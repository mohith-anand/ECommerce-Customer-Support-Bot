import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.utils import load_data, clean_text

# Embedding model
EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

# Paths
INDEX_PATH = "vectorstore/faiss_index.bin"
TEXTS_PATH = "vectorstore/texts.npy"

def build_faiss_index(data_dir="data/"):
    texts = []
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)
        if os.path.isfile(path):
            content = load_data(path)
            texts.append(clean_text(content))
    if not texts:
        texts = ["No documents available."]
    embeddings = EMBEDDING_MODEL.encode(texts, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    os.makedirs("vectorstore", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    np.save(TEXTS_PATH, np.array(texts, dtype=object))
    print(f"FAISS index built with {len(texts)} documents.")

def load_faiss_index():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(TEXTS_PATH):
        build_faiss_index()
    index = faiss.read_index(INDEX_PATH)
    texts = np.load(TEXTS_PATH, allow_pickle=True)
    # Return structured docs
    docs = [{"id": f"doc_{i+1}", "text": t} for i, t in enumerate(texts)]
    return index, docs

def retrieve(query, k=3):
    index, docs = load_faiss_index()
    q_vec = EMBEDDING_MODEL.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_vec, k)
    results = [docs[i] for i in indices[0]]
    return results
