
# Make A QRCode
import pyqrcode

url = pyqrcode.create('http://www.faileap.com')
url.svg('faileap.svg',scale=8)
url.eps('faileap.eps',scale=2)

print(url.terminal(quiet_zone=1))
