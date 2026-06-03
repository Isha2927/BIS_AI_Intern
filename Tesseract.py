import pytesseract
from PIL import Image

images = [
    "invoice.webp",
    "receipt.webp",
    "scanneddocument.webp"
]

for image_file in images:
    print("\n" + "="*50)
    print("Processing:", image_file)
    print("="*50)

    img = Image.open(image_file)
    text = pytesseract.image_to_string(img)

    print(text)