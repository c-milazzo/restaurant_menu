import qrcode

image = qrcode.make("https://127.0.01:800")
image.save("qr.png")