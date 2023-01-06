# # Simple generation QR Code
# import qrcode as qr

# img = qr.make("https://youtu.be/OKuiyX5k6zg") 
# img.save("YouTube WsCube.png")

# QR Code generation

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10, border=4)

qr.add_data("https://youtu.be/OKuiyX5k6zg")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "blue")
img.save("QR2.png")