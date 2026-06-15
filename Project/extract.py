from paddleocr import PaddleOCR

# Initialize OCR model
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en'
)

def extract_text(image_path):

    result = ocr.ocr(image_path)

    extracted_text = ""

    for line in result[0]:
        text = line[1][0]
        extracted_text += text + "\n"

    return extracted_text