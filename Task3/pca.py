from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "I love machine learning",
    "Artificial intelligence is fascinating",
    "Cats are cute animals",
    "Dogs are loyal pets",
    "Deep learning uses neural networks"
]

# Generate embeddings
embeddings = model.encode(sentences)
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(reduced[:, 0], reduced[:, 1])

for i, txt in enumerate(sentences):
    plt.annotate(txt, (reduced[i, 0], reduced[i, 1]))

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Sentence Embeddings Visualized using PCA")
plt.show()