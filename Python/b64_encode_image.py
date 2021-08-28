import tkinter as tk
from tkinter import filedialog
import base64
import sys
import pyperclip

root = tk.Tk()
root.withdraw()
root.clipboard_clear()

file_path = filedialog.askopenfilename()
extension = ""
if file_path.endswith('.jpg'):
    extension = "jpg"
elif file_path.endswith('.png'):
    extension = "png"
else:
    print("Incompatible image type, exiting!")
    sys.exit()

image_description = input("Enter an image description: ")

with open(file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    pyperclip.copy(f"<img src='data:image/{extension};base64,{encoded_string.decode('utf-8')}'>{image_description}</img>")
    print("Base64 encoded image tag has been copied to the clipboard.")

    
answer = input("Do you want to delete the image? Y/N: ".rstrip())
if answer == 'y' or 'Y':
    os.remove(file_path)
