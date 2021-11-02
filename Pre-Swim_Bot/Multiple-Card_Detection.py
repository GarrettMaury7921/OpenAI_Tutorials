import cv2 as cv
import numpy as np
import os

template = cv.imread('image_assets/cards/template3.png', cv.IMREAD_REDUCED_COLOR_2)
img = cv.imread('image_assets/cards/rearguard.png', cv.IMREAD_REDUCED_COLOR_2)

# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
result = cv.matchTemplate(template, img, cv.TM_SQDIFF_NORMED)

# I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
threshold = 0.17
locations = np.where(result <= threshold)

# We can zip those up into a list of (x, y) position tuples
locations = list(zip(*locations[::-1]))
# print(locations)

if locations:
    print('Found needle.')

    width = img.shape[1]
    height = img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
    for loc in locations:
        # Determine the box positions
        top_left = loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        # Draw the box
        cv.rectangle(template, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches', template)
    cv.waitKey()
    # cv.imwrite('result.jpg', haystack_img)

else:
    print('Needle not found.')
