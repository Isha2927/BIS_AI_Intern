from PIL import Image
from paddleocr import PaddleOCR

img = Image.open("bounding box.webp")

table_region = img.crop((10, 120, 210, 250))

table_region.save("table_region.webp")

ocr = PaddleOCR(use_angle_cls=True, lang='en')

result = ocr.ocr("table_region.webp", cls=True)

print("Table Content:")

for line in result[0]:
    print(line[1][0])