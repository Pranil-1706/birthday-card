# Install first:
# pip install qrcode[pil]

import qrcode

url = "https://pranil-1706.github.io/birthday-card/"

qr = qrcode.QRCode(
    version=None,  # auto size
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # more reliable scanning
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("birthday_qr.png")

print("Saved: birthday_qr.png")
