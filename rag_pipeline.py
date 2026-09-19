import os
import chromadb
from groq import Groq
from sentence_transformers import SentenceTransformer
from document_processor import extract_content

class MultimodalRAG:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path="storage/chroma")
        self.collection = self.client.get_or_create_collection("visionvault")
        self.llm = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _chunks(self, text, size=900, overlap=120):
        text = " ".join(text.split())
        step = size - overlap
        return [text[i:i + size] for i in range(0, len(text), step) if text[i:i + size].strip()]

    def ingest_files(self, files):
        total = 0
        for file in files:
            text, source = extract_content(file)
            chunks = self._chunks(text)
            if not chunks:
                continue
            vectors = self.embedder.encode(chunks).tolist()
            ids = [f"{source}_{i}_{abs(hash(chunk))}" for i, chunk in enumerate(chunks)]
            self.collection.upsert(
                ids=ids,
                documents=chunks,
                embeddings=vectors,
                metadatas=[{"source": source} for _ in chunks]
            )
            total += len(chunks)
        return total

    def ask(self, question):
        vector = self.embedder.encode([question]).tolist()
        result = self.collection.query(query_embeddings=vector, n_results=5)
        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]

        if not docs:
            return "No relevant information found.", []

        context = "\n\n".join(
            f"Source: {meta['source']}\n{doc}"
            for doc, meta in zip(docs, metas)
        )
        prompt = f"""Answer only from the context below.
If the answer is missing, say that it is not available.
Do not invent facts.

CONTEXT:
{context}

QUESTION:
{question}"""

        response = self.llm.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=1200
        )
        sources = list(dict.fromkeys(meta["source"] for meta in metas))
        return response.choices[0].message.content, sources

    def clear_database(self):
        try:
            self.client.delete_collection("visionvault")
        except Exception:
            pass
        self.collection = self.client.get_or_create_collection("visionvault")
