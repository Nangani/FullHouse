"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""
import sys
import math
import cv2 as cv
import numpy as np


def main(argv):
    ## [load]
    default_file =  "123.png"
    filename = argv[0] if len(argv) > 0 else default_file

    # Loads an image
    src = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    i1 = cv.imread(filename, cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    ## [load]

    ## [edge_detection]
    # Edge detection
    dst = cv.Canny(src, 100, 200, None, 3)
    ## [edge_detection]


    lower = np.array([0])
    upper = np.array([10])
    hsvi = cv.cvtColor(i1, cv.COLOR_BGR2HSV)
    mask = cv.inRange(src, lower, upper)
    cv.imshow("1", src)
    cv.imshow("2", mask)
    cv.imshow("3", hsvi[:,:,2])
    lower1 = np.array([[[0, 0, 0]]])
    upper1 = np.array([[[20, 60, 40]]])
    mask2 = hsvi[:,:,2]
    #mask2 = cv.inRange(hsvi, lower1, upper1)
    cv.imshow("4", i1)
    cv.imshow("5", mask2)
    mask3 = cv.inRange(mask2, lower1, upper1)
    cv.imshow("6", mask3)

    black = np.uint8([[[0, 0, 0]]])
    hsv_black = cv.cvtColor(black, cv.COLOR_BGR2HSV)
    print(hsv_black)

    lower2 = np.array([0, 0, 0])
    upper2 = np.array([80, 80, 80])
    asdf = cv.inRange(i1, lower2, upper2)
    cv.imshow("7", asdf)

    #hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    #lower = np.array
    #mask = cv.inRange(hsv, lower, upper)

    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(mask3, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    ## [hough_lines]
    #  Standard Hough Line Transform
    lines = cv.HoughLines(mask3, 1, np.pi / 180, 150, None, 0, 0)
    ## [hough_lines]
    ## [draw_lines]
    # Draw the lines
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    ## [draw_lines]

    ## [hough_lines_p]
    # Probabilistic Line Transform
    linesP = cv.HoughLinesP(mask3, 1, np.pi / 180, 20, None, 5, 10)
    ## [hough_lines_p]
    ## [draw_lines_p]
    # Draw the lines
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    ## [draw_lines_p]
    ## [imshow]
    # Show results
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    ## [imshow]
    ## [exit]
    # Wait and Exit
    cv.waitKey()
    return 0
    ## [exit]

if __name__ == "__main__":
    main(sys.argv[1:])
