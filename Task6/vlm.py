from google import genai
from PIL import Image

client = genai.Client(api_key="API_KEY")

image_path = input("Enter image path: ")
question = input("Ask a question: ")

image = Image.open(image_path)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[question, image]
)

print("\nAnswer:")
print(response.text)