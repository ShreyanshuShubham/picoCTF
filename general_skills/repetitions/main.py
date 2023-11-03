import base64,re

data = open("enc_flag","r").read()

while not data.startswith("pico"):
    data = base64.b64decode(data).decode()
    print(data)
