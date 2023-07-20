import qrcode
from PIL import Image
import os

def print_green(text):
    GREEN = '\033[92m'
    RESET = '\033[0m'
    print(GREEN + text + RESET)

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen

python_logo = r"""
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█
"""

print(python_logo)
print_green("       POLAT QR CODE GENERATOR")

try:
    qr = qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
    )

    data = input("Please enter the content you want to create a QR Code for: ")

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_path = input("Where and with what name do you want to save the image (include the extension, e.g. .png): ")
    img.save(img_path)
    print_green("QR code image successfully created and saved!")

except Exception as e:
    print_green("An error occurred: " + str(e))
