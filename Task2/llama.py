from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Explain Machine Learning in simple terms."
        }
    ]
)

print(response.choices[0].message.content)