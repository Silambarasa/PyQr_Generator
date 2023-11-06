import pyqrcode

Qr_link = "www.linkedin.com/in/silambarasan-perumal"
url = pyqrcode.create(Qr_link)
url.png('qr_image',scale=5)