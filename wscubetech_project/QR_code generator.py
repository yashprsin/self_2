import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("hello everyone")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("SampleV2.png")

"""
# Simple qrcode

import qrcode as qr
img = qr.make('Hello world')
img.save("some.png")
"""
