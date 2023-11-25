from PIL import Image

def encode_image(source_img_path, secret_msg, output_img_path):
    img = Image.open(source_img_path)
    width, height = img.size

    secret_msg += "###"  # Add a delimiter to mark the end of the message
    binary_secret_msg = ''.join(format(ord(char), '08b') for char in secret_msg)

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            for color_channel_index in range(3):  # RGB channels
                if data_index < len(binary_secret_msg):
                    pixel[color_channel_index] = int(format(pixel[color_channel_index], '08b')[:-1] + binary_secret_msg[data_index], 2)
                    data_index += 1

            img.putpixel((x, y), tuple(pixel))

            if data_index == len(binary_secret_msg):
                break

    img.save(output_img_path)

def decode_image(encoded_img_path):
    img = Image.open(encoded_img_path)
    binary_secret_msg = ''

    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            for color_channel_index in range(3):
                binary_secret_msg += format(pixel[color_channel_index], '08b')[-1]

    secret_msg = ''
    for i in range(0, len(binary_secret_msg), 8):
        byte = binary_secret_msg[i:i+8]
        secret_msg += chr(int(byte, 2))
        if secret_msg[-3:] == "###":  # Check for the delimiter
            break

    return secret_msg[:-3]



source_image = input("Enter the image name with extension: ")
output_image = "output_image.png"
message_to_hide = input("Enter Message To Hide: ")

encode_image(source_image, message_to_hide, output_image)
decoded_message = decode_image(output_image)
print("Decoded Message:", decoded_message)