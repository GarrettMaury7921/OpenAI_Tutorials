from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

while True:
    if pyautogui.locateOnScreen('image_assets/main_menu') is not None:
        print('I can see it!')
        time.sleep(0.5)
    else:
        print('I cannot see it...')
        time.sleep(0.5)