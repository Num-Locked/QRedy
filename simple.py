import qrcode

data = (input ('data/link \n'))
filename = (input ('file name \n'))

img = qrcode.make(data)

print ('Done!')

img.save (filename)

#this is just s simple qr code maker.
#mostly made for me but feel free to use this
