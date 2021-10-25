import 路由器设置or登录
import 路由器抓包
import pynput
from pynput.keyboard import Controller
import time
keyboard1 = Controller()
from pynput.mouse import Controller,Button
mouse1 = Controller()

l={}
speed=30
# 键盘监听
from pynput.keyboard import Listener

def panduanzuhejian(key):
    if str(key) == "'q'" and 'Key.alt_l' in l:
        return 1
    elif str(key) == "'w'" and 'Key.alt_l' in l:
        return 2
    elif str(key) == "'xx'" and 'Key.alt_l' in l:
        return 3
    elif str(key) == "'e'" and 'Key.alt_l' in l:
        return 4

    elif str(key) == "'z'" and 'Key.alt_l' in l:
        return 5
    elif str(key) == "'x'" and 'Key.alt_l' in l:
        return 6



    elif (str(key) == "'w'" and "'l'" in l) or str(key) == "<104>":
        return 'up'
    elif (str(key) == "'s'" and "'l'" in l) or str(key) == "<101>":
        return 'down'
    elif (str(key) == "'a'" and "'l'" in l) or str(key) == "<100>":
        return 'left'
    elif (str(key) == "'d'" and "'l'" in l) or str(key) == "<102>":
        return 'right'
    elif (str(key) == "'j'" and "'l'" in l) or str(key) == "<97>":
        return 'click_l'
    elif (str(key) == "'k'" and "'l'" in l) or str(key) == "<99>":
        return 'click_r'
    elif (str(key) == "'xxj'" and "'xxl'" in l) or str(key) == "<103>":
        return 'scroll_up'
    elif (str(key) == "'xxk'" and "'xxl'" in l) or str(key) == "<105>":
        return 'scroll_down'
    #scroll(0, -100)



def on_press(key):

    print('按下' + str(key))
    l[str(key)] = 0
    print(l)

    if panduanzuhejian(key) == 1:
        print(mouse1.position)
        a=mouse1.position
        mouse1.position = (1919,1079)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.1)
        mouse1.position=(260,1061)
        mouse1.click(pynput.mouse.Button.left,1)
        time.sleep(0.3)
        mouse1.position = (80,15)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.1)
        mouse1.position = a

    elif panduanzuhejian(key)==2:
        a = mouse1.position

        mouse1.position = (894,312)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.3)

        mouse1.position = (1434,952)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.5)

        mouse1.position = (1005,310)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.4)
        mouse1.position = a
    elif panduanzuhejian(key)==3:


        a = mouse1.position

        mouse1.position = (1652,1058)
        mouse1.click(pynput.mouse.Button.right, 1)

        mouse1.position = (1652, 1058)
        keyboard1.press('h')
        keyboard1.release('h')
        time.sleep(1)

        mouse1.position = (1652, 1058)

        #mouse1.click(pynput.mouse.Button.right, 1)
        #time.sleep(1.5)
        #mouse1.position = (1544,994)
        #mouse1.position = (1706,910)
        #mouse1.click(pynput.mouse.Button.left, 1)



        #mouse1.position = (968,664)
        #mouse1.click(pynput.mouse.Button.left, 1)
        #time.sleep(1)

        mouse1.position = (1272,344)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.5)


        #mouse1.position = a


    elif panduanzuhejian(key) == 4:
        a = mouse1.position
        mouse1.position = (174, 1061)
        mouse1.click(pynput.mouse.Button.left, 1)
        time.sleep(0.1)
        mouse1.position = a


    elif panduanzuhejian(key) == 5:
        try:
            路由器设置or登录.main1()
        except:
            pass

    elif panduanzuhejian(key) ==6:
        try:
            路由器抓包.main1()
        except:
            pass


    elif panduanzuhejian(key) =='up':
        mouse1.move(0,-speed)
    elif panduanzuhejian(key) =='down':
        mouse1.move(0,speed)
    elif panduanzuhejian(key) =='left':
        mouse1.move(-speed,0)
    elif panduanzuhejian(key) =='right':
        mouse1.move(speed,0)
    elif panduanzuhejian(key) =='click_l':
        mouse1.click(Button.left,1)
    elif panduanzuhejian(key) =='click_r':
        mouse1.click(Button.right,1)
    elif panduanzuhejian(key) =='scroll_up':
        mouse1.scroll(0,4)
    elif panduanzuhejian(key) =='scroll_down':
        mouse1.scroll(0,-4)




def on_release(key):
    print('松开'+str(key))
    if "'l'" in l and ("'w'" in l)or("'a'" in l)or("'s'" in l)or("'d'" in l):
        l.clear()
        l["'l'"]=0

    else:
        l.clear()




#监听键盘按键
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
#停止监视
Listener.stop()