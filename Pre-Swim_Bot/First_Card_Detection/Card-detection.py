import cv2 as cv
import os

# Can use IMREAD flags to do different pre-processing of image files,
# like making them grayscale or reducing the size.
template = cv.imread('image_assets/cards/template2.png', cv.IMREAD_REDUCED_COLOR_2)
img = cv.imread('image_assets/cards/corsair.png', cv.IMREAD_REDUCED_COLOR_2)


# There are 6 comparison methods to choose from:
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
# You can see the differences at a glance here:
# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
result = cv.matchTemplate(template, img, cv.TM_CCOEFF_NORMED)


# Get the best match position from the match result.
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found card.')

    wid = img.shape[1]
    hei = img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + wid, top_left[1] + hei)

    cv.rectangle(template, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', template)
    cv.waitKey()

else:
    print('Not found')

