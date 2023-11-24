import stepic
from PIL import Image
from cryptography.fernet import Fernet


def encoding():
    print("-------------------------------------")
    key = Fernet.generate_key()
    print("Random Password is: ", key)
    enc = Fernet(key)
    text = input("Enter the hiding mesage: ")
    text_enc = enc.encrypt(text.encode())
    file = input("Photo: ")
    img = Image.open(file)
    img_stegano = stepic.encode(img, text_enc)
    img_stegano.save("output.png")
    print("-------------------------------------")
    input("COMPLETE (press enter -> exit)")


def decoding():
    print("-------------------------------------")
    key=input("Enter Password To Decode: ")
    dec=Fernet(key)
    decoding_img = Image.open("output.png")
    decoded=stepic.decode(decoding_img)
    text_dec=dec.decrypt(decoded.encode())
    print("The Hidden Message is  : "+text_dec.decode())
    print("-------------------------------------")
encoding()
decoding()