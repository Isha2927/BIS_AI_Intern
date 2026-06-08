from transformers import pipeline

# Create summarizer
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# Read transcript
with open("transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# Generate summary
summary = summarizer(
    transcript,
    max_length=80,
    min_length=20,
    do_sample=False
)

print("\nSUMMARY:\n")
print(summary[0]["summary_text"])