import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time

loop_time = time()
while True:

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    print('Done.')
