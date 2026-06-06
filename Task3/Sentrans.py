from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love machine learning",
    "Artificial intelligence is fascinating",
    "Cats are cute animals",
    "Dogs are loyal pets",
    "Deep learning uses neural networks"
]

embeddings = model.encode(sentences)

print(embeddings.shape)
print(embeddings[0][:10])