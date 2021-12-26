import cv2 as cv
from time import time
from WindowCapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter

# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_limestone = Vision('images/thumb.jpg')
# initialize the trackbar window
# vision_limestone.init_control_gui()

# example limestone HSV filter
# hsv_filter = HsvFilter(0, 180, 129, 15, 229, 243, 143, 0, 67, 0)

loop_time = time()
while True:

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # # pre-process the image
    # processed_image = vision_limestone.apply_hsv_filter(screenshot)
    #
    # # object detection
    # rectangles = vision_limestone.find(processed_image, 0.5)
    #
    # # draw the detection results onto the original image
    # output_image = vision_limestone.draw_rectangles(screenshot, rectangles)

    # resize the windows
    output_image = cv.resize(screenshot, (900, 500))
    # processed_image = cv.resize(processed_image, (900, 500))

    # Display the processed image and
    cv.imshow('Matches', output_image)
    # cv.imshow('Processed', processed_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('z'):
        cv.imwrite('AI_Cascade_Classifier/data/positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('x'):
        cv.imwrite('AI_Cascade_Classifier/data/negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')
