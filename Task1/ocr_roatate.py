from paddleocr import PaddleOCR
from PIL import Image

ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Run OCR
result = ocr.ocr("rotated_invoice.webp", cls=True)

# Print extracted text
for line in result[0]:
    print(line[1][0])