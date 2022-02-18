from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(r"C:\Users\lotar\Desktop\projets\qr_code_encoder_decoder\files\myqrcode.png")

result = decode(img)

print(result)
