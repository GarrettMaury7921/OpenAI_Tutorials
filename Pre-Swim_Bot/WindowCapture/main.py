import cv2 as cv
from time import time, sleep
from WindowCapture import WindowCapture

# Get the names of all windows running
# WindowCapture.list_window_names()
# exit()

# initialize the WindowCapture class
Window_Capture = WindowCapture()

loop_time = time()
while True:

    # get an updated image of the game
    screenshot = Window_Capture.get_screenshot()

    screenshot = cv.resize(screenshot, (600, 400))
    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
