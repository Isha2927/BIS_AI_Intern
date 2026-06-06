from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love machine learning",
    "Artificial intelligence is fascinating",
    "Cats are cute animals",
    "Dogs are loyal pets",
    "Deep learning uses neural networks"
]

embeddings = model.encode(sentences)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

query = "AI and neural networks"

query_embedding = model.encode([query])

D, I = index.search(np.array(query_embedding), k=2)

print("Query:", query)

for idx in I[0]:
    print(sentences[idx])