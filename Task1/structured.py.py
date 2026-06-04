from paddleocr import PPStructure
import cv2

table_engine = PPStructure(show_log=True)

img = cv2.imread("table.webp") 

result = table_engine(img)

for line in result:
    print(line)