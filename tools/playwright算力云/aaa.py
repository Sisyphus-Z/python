import keyboard
import pyautogui


def t(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == "h":

        pyautogui.hotkey('alt', 'f4')


keyboard.hook(t)

input()