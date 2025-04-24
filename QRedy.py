import qrcode

print ('Hello! welcome to my Shitty program!')

#details for the qr code
link = (input('Enter Your data to make the QR code \n'))
version = (input ('What version.If not sure say 1.Max is 40 \n'))
box_size = (input ('Box size. \n'))
border = (input('Alright now border.if not sure say 1 \n'))
name = (input ('And finally what should it be called \n'))

img = qrcode.make(link)

#code shit i pulled of the qrcode extension on pypi
qr = qrcode.QRCode(
    version=(version),
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=(box_size),
    border=(border),
)

#finishes making qr code
print ('Done!')

img.save (name)