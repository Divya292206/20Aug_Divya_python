import qrcode

url = "https://www.tops-int.com/"

# Create QR code
qr = qrcode.make(url)

# Save QR code image
qr.save('qrcode.png')

print("QR Code Generated Successfully")
