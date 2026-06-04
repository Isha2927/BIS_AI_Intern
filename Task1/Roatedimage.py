from PIL import Image

img = Image.open("invoice.webp")

rotated = img.rotate(15, expand=True)

rotated.save("rotated_invoice.webp")

print("Rotated image saved!")