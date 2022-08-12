import pyqrcode

address = 'google.com'
url = pyqrcode.create(address)
url.png('google.png', scale=8)
