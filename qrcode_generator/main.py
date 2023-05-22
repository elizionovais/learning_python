import qrcode

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# The data that you want to store
data = input("Enter the data to be encoded: ")
name = input("Enter the name of the file: ")

img = qrcode.make(data)

# Create and save the file
img.save(f"{name}.jpg")
