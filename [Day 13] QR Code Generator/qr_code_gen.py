import qrcode
img = qrcode.make('https://m3galodn81.github.io/')
type(img)
img.save("link.png")