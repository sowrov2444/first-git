a=10
b=5
print(a+b)
#comand line
import sys
print(sys.argv)
print(type(sys.argv))
arguments=sys.argv
a = arguments[1]
b = arguments[2]
print(sum(a+b))
a=["add.py",3,6]

#from pytube import YouTube
from pytube import YouTube
url=""
yt=YouTube(url)
video_stream=yt.streams.get_highest_resolution()
video_stream.download()
print("downloades successfully!")

import qrcode
def generate_qr_code(data, size=200):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Adjust box_size according to your preference
        border=4,     # Adjust border according to your preference
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")
    img = img.resize((size, size))  # Resize the image to the specified size
    return img
data = "https://youtu.be/m5Lgc1upeOw"
size = 400  # Specify the desired size of the QR code
qr_code = generate_qr_code(data, size)
qr_code.show()


import qrcode
def file(data, size=200):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Adjust box_size according to your preference
        border=4,

    )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_ecoller="bluee",back_color="red")
    img=img.resize((size,size))
    return img
data="https://youtu.be/S7v9J-ac7KM"
size=400
qr_code=file(data,size)
qr_code.show()


import qrcode
def hello(data,size=200):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_coller="green",back_coller="red")
    img=img.resize((size,size))
    return img
data="https://youtu.be/S7v9J-ac7KM"
size=400
qr_code=hello(data,size)
qr_code.show()








