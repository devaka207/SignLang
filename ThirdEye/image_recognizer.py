import pytesseract
from PIL import Image
import os

def take_read_pic():
    os.system("test.jpg")
    print(pytesseract.image_to_string(Image.open('test.jpg') ))
