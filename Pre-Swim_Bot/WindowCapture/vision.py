import cv2 as cv
import numpy as np
import os


def find_click_positions(img_path, template, threshold=0.5, debug_mode=None):
    img = cv.imread(img_path, cv.IMREAD_REDUCED_COLOR_2)
    # Width and height
    width = img.shape[1]
    height = img.shape[0]

    # Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
    result = cv.matchTemplate(template, img, cv.TM_SQDIFF_NORMED)

    # I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
    threshold = 0.17
    locations = np.where(result <= threshold)

    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    # print(locations)

    # GROUP RECTANGLES
    # First we need to create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), width, height]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)

    # 3rd param, higher = easier to find cards, lower =
    # harder to find cards but less likely for rectangles to choose the same card
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.1)

    # print(rectangles)  # Print where cards are

    points = []
    if len(rectangles):
        # print('Found card.')

        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the locations and draw their rectangle
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            # Save the points
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                # Determine the box position
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Draw the box
                cv.rectangle(template, top_left, bottom_right, color=line_color,
                             lineType=line_type, thickness=2)
            elif debug_mode == 'points':
                # Draw the center point
                cv.drawMarker(template, (center_x, center_y),
                              color=marker_color, markerType=marker_type,
                              markerSize=40, thickness=2)

    if debug_mode:
        cv.imshow('Matches', template)
        # cv.waitKey()
        # cv.imwrite('result_click_point.jpg', haystack_img)

    return points