import easyocr

reader = easyocr.Reader(['en'])

images = [
    "invoice.webp",
    "receipt.webp",
    "scanneddocument.webp"
]

for image in images:
    print("\n" + "="*50)
    print("Processing:", image)
    print("="*50)

    result = reader.readtext(image)

    for item in result:
        print(item[1])