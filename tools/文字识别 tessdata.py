# https://github.com/UB-Mannheim/tesseract/wiki
# https://github.com/tesseract-ocr/tessdata

import pytesseract
from PIL import ImageGrab
import os

def tesseract1():
    img1 = ImageGrab.grabclipboard()

    img1.save('pic_temp.png','PNG')

    pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract-OCR\tesseract'

    text1=pytesseract.image_to_string('pic_temp.png')

    with open('text_temp.txt','w',encoding='gbk') as f:
        f.write(text1)

    os.system('text_temp.txt')


import threading
import time

from pynput import mouse, keyboard

mouse1 = mouse.Controller()
keyboard1 = keyboard.Controller()



def on_click(x, y, button, pressed):
    pass


def on_press(key):
    if str(key) == "'`'":
        try:
            tesseract1()
        except Exception as r:
            print(r)
            return

def on_release(key):
    pass



def listen_keyboard():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


t_K = threading.Thread(target=listen_keyboard)
t_K.start()


t_K.join()

