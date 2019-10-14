import os, qrtools, time
 
qr = qrtools.QR()
s = "lJ9YVeeA9kjT5wcnLu9y"
while True:
    os.system("curl http://tunnel.web.easyctf.com/images/%s.png > code.png" % s)
    qr.decode("code.png")
    s = qr.data
    print s