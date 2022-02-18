import qrcode


data = r"Don't forget to subscribe"

my_qr = r"C:\Users\lotar\Desktop\projets\qr_code_encoder_decoder\files\myqrcode.png"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save(my_qr)
