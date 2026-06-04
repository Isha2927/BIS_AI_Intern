from paddleocr import PaddleOCR
from PIL import Image

# Create rotated image
img = Image.open("invoice.webp")
rotated = img.rotate(15, expand=True)
rotated.save("rotated_invoice.webp")

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Compare Original vs Rotated
images = {
    "Original Image": "invoice.webp",
    "Rotated Image": "rotated_invoice.webp"
}

for title, image_path in images.items():
    print("\n" + "="*60)
    print(title)
    print("="*60)

    result = ocr.ocr(image_path, cls=True)

    for line in result[0]:
        print(line[1][0])