from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Documents with metadata
documents = [
    {"text": "I love machine learning", "category": "AI"},
    {"text": "Deep learning uses neural networks", "category": "AI"},
    {"text": "Artificial intelligence is fascinating", "category": "AI"},
    {"text": "Cats are cute animals", "category": "Animals"},
    {"text": "Dogs are loyal pets", "category": "Animals"}
]

# Extract text
texts = [doc["text"] for doc in documents]

# Create embeddings
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Query
query = "Neural network applications"

# Metadata filter
selected_category = "AI"

# Filter documents
filtered_docs = [
    doc for doc in documents
    if doc["category"] == selected_category
]

filtered_texts = [doc["text"] for doc in filtered_docs]

# Generate embeddings for filtered docs
filtered_embeddings = model.encode(filtered_texts)

# Temporary index
filtered_index = faiss.IndexFlatL2(filtered_embeddings.shape[1])
filtered_index.add(np.array(filtered_embeddings))

# Search
query_embedding = model.encode([query])

D, I = filtered_index.search(
    np.array(query_embedding),
    k=2
)

print(f"\nSearching only in category: {selected_category}\n")

for idx in I[0]:
    print(filtered_texts[idx])