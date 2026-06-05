import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LddqRtlaO3PfHh8bc1ydfP9n9pPvCeuq_a_9-mmfdIbg")

model = genai.GenerativeModel("gemini-2.5-flash")

prompts = [
    "Explain Machine Learning in simple terms.",
    "Summarize the importance of cloud computing in 100 words.",
    "Write a professional email requesting an internship opportunity."
]

for i, prompt in enumerate(prompts, start=1):
    print("\n" + "="*60)
    print(f"PROMPT {i}")
    print("="*60)

    response = model.generate_content(prompt)

    print(response.text)