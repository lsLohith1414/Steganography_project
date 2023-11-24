
import cv2
import os

def text_to_hex(secret_msg):
    hexa_text = secret_msg.encode('utf-8').hex()
    return hexa_text
def hex_to_text(hexa_text):
    decrypt_bytes = bytes.fromhex(hexa_text)
    decrypted_text = decrypt_bytes.decode('utf-8')
    return decrypted_text



image_name = input("Enter the image name with extension: ")
image = cv2.imread(image_name)
passcode = input("Enter the password: ")
secret_message = input("Enter the secret message: ")
encrypted_msg = text_to_hex(secret_message)
character_to_code={}
code_to_character={}
for i in range(255):
    character_to_code[chr(i)]=i
    code_to_character[i]=chr(i)

n=0
m=0
for i in range(len(encrypted_msg)):
    image[n, m, 0] = character_to_code[encrypted_msg[i]]
    n += 1
    m += 1

cv2.imwrite('encrypt_image_new.jpg', image)
os.system('encrypt_image_new.jpg')

decrypt_msg = ""
n = 0
m = 0

password = input("Enter the password for decryption: ")
if password == passcode:
    for i in range(len(encrypted_msg)):
        decrypt_msg = decrypt_msg + code_to_character[image[n, m, 0]]
        n += 1
        m += 1

    print("Decrypted message is:", hex_to_text(decrypt_msg))
else:
    print("Invalid password")