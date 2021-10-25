parameter1=1

import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()




def on_scroll(x, y, dx, dy):
    if dy>0:
        keyboard1.press(keyboard.Key.left)
        keyboard1.release(keyboard.Key.left)
    elif dy<0:
        keyboard1.press(keyboard.Key.right)
        keyboard1.release(keyboard.Key.right)



def on_press(key):
    print(key)

def on_release(key):
    print(key)

def listen_mouse():
    with mouse.Listener(on_scroll=on_scroll) as listener:
        listener.join()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



t_m=threading.Thread(target=listen_mouse)
t_m.start()

t_k=threading.Thread(target=listen_keyboard)
t_k.start()


t_m.join()
t_k.join()