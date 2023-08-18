import threading
import time

from pynput import mouse,keyboard
mouse1=mouse.Controller()
keyboard1=keyboard.Controller()

pos=[9999,9999]
ispressed=False
shoushi=None

def panduanshoushi(x,y):
    global shoushi

    if y-pos[1]>=200 and abs(x-pos[0])<=150 and shoushi==None:
        shoushi='down'

    elif x-pos[0]>=200 and abs(y-pos[1])<=150 and shoushi==None:
        shoushi='right'

    elif pos[0]-x>=200 and abs(y-pos[1])<=150 and shoushi==None:
        shoushi='left'




def on_move(x, y):
    if ispressed==True:
        panduanshoushi(x, y)


def on_click(x, y, button, pressed):
    global ispressed
    global shoushi

    if str(button)=='Button.right' and pressed==True:
        pos[0]=mouse1.position[0]
        pos[1] = mouse1.position[1]

        ispressed=True
        print(mouse1.position)



    elif pressed==False:

        print(shoushi)
        if shoushi=='down':
            time.sleep(0.35)
            keyboard1.press(keyboard.Key.esc)
            keyboard1.release(keyboard.Key.esc)
            keyboard1.press(keyboard.Key.ctrl)
            keyboard1.press('w')
            time.sleep(0.4)
            keyboard1.release(keyboard.Key.ctrl)
            keyboard1.release('w')
        elif shoushi=='left':
            time.sleep(0.35)
            keyboard1.press(keyboard.Key.esc)
            keyboard1.release(keyboard.Key.esc)

            keyboard1.press(keyboard.Key.ctrl_l)
            keyboard1.press(keyboard.Key.shift_l)
            keyboard1.press(keyboard.Key.tab)
            time.sleep(0.4)
            keyboard1.release(keyboard.Key.ctrl_l)
            keyboard1.release(keyboard.Key.shift_l)
            keyboard1.release(keyboard.Key.tab)
        elif shoushi=='right':
            time.sleep(0.35)
            keyboard1.press(keyboard.Key.esc)
            keyboard1.release(keyboard.Key.esc)

            keyboard1.press(keyboard.Key.ctrl_l)
            keyboard1.press(keyboard.Key.tab)
            time.sleep(0.4)
            keyboard1.release(keyboard.Key.ctrl_l)
            keyboard1.release(keyboard.Key.tab)

        shoushi=None
        ispressed=False

def on_scroll(x, y, dx, dy):
    # print('Scrolled {0} at {1}'.format(
    #
    #     'down' if dy < 0 else 'up', (x, y)))
    pass


def on_press(key):
    pass
def on_release(key):
    pass


def listen_mouse():
    with mouse.Listener(on_move=on_move, on_click=on_click,on_scroll=on_scroll) as listener:
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

