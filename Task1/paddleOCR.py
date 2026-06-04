from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

images = [
    "invoice.webp",
    "receipt.webp",
    "scanneddocument.webp"
]

for image in images:
    print("\n" + "="*50)
    print("Processing:", image)
    print("="*50)

    result = ocr.ocr(image)

    for line in result[0]:
        print(line[1][0])