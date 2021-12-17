import cv2 as cv
from time import time, sleep
import pyautogui
import numpy as np
import pygetwindow

from vision import find_click_positions


# Get the names of all windows running
# WindowCapture.list_window_names()
# exit()

loop_time = time()
while True:

    # get an updated image of the game
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    screenshot = cv.resize(screenshot, (900, 400))
    # NOTE: If you get a AttributeError: 'NoneType' object has no attribute 'shape'
    # This means the picture is wrong (location)
    find_click_positions('images/thumb.png', screenshot, 0.9, 'rectangles')
    # cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
