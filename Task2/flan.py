from transformers import pipeline

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

result = pipe(
    "Explain Machine Learning in simple terms.",
    max_length=100
)

print(result[0]["generated_text"])