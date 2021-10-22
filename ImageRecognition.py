from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

x = 0
while 1:
    # MAY CHANGE IF YOU CHANGE COMPUTERS
    # MUST BE SHIFT + (Windows Key) + S FOR SCREENSHOT
    if pyautogui.locateOnScreen('image_assets/main_menu.png', confidence=.9) is not None:
        print('I can see it!')
        time.sleep(0.5)
        break
    else:
        print('I cannot see it...')
        print(x)
        x = x+1
        time.sleep(0.5)
