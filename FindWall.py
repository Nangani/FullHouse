"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""
import sys
import math
import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageDraw
import requests

def isWaterMark(hsv, j1, i1, j2, i2):
    if -3 <= int(hsv[j1, i1][0]) - int(hsv[j2, i2][0]) and int(hsv[j1, i1][0]) - int(hsv[j2, i2][0]) <= 3 and -60 <= int(hsv[j1, i1][1]) - int(hsv[j2, i2][1]) and int(hsv[j1, i1][1]) - int(hsv[j2, i2][1]) <= 0\
            and 0 <= int(hsv[j1, i1][2]) - int(hsv[j2, i2][2]) and int(hsv[j1, i1][2]) - int(hsv[j2, i2][2]) <= 30 and int(hsv[j2, i2][2]) <= 25:
        return True
    else:
        return False

def main(argv):
    default_file =  "plan3.jpg"
    filename = argv[0] if len(argv) > 0 else default_file

    # Loads an image
    src = cv.imread(filename, cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1

    hsvImage = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    cv.imshow("hsvImage", hsvImage)
    lower = np.array([[[0, 0, 0]]])
    upper = np.array([[[255, 255, 45]]])
    mask = cv.inRange(hsvImage, lower, upper)

    cv.imshow("mask", mask)

    aaaa = Image.open(default_file)
    (width, height) = aaaa.size
    print(width)
    print(height)
    print(hsvImage[280, 200])
    #(width, height) = hsvi.size
    for i in range(1, width-1):
        for j in range(1, height-1):
            if j - 1 >= 0 and isWaterMark(hsvImage, j, i, j - 1, i):
               # print(hsvi[j, i])
                #print(hsvi[j-1, i])
               # print((int(hsvi[j, i][1]) + int(hsvi[j-1, i][1])) / 2)
               # print(hsvi[j, i][1])
               #
               hsvImage[j, i][0] = hsvImage[j - 1, i][0]
               hsvImage[j, i][1] = hsvImage[j - 1, i][1]
               hsvImage[j, i][2] = hsvImage[j - 1, i][2]

               #hsvi[j, i][1] = (int(hsvi[j, i][1]) + int(hsvi[j-1, i][1])) / 2
               #hsvi[j, i][2] = (int(hsvi[j, i][2]) + int(hsvi[j-1, i][2])) / 2

            #elif j + 1 < height and isWaterMark(hsvi, j, i, j + 1, i):
             #   hsvi[j, i][1] = hsvi[j+1, i][1]
              #  hsvi[j, i][2] = hsvi[j+1, i][2]

            elif i - 1 >= 0 and isWaterMark(hsvImage, j, i, j, i - 1):
                hsvImage[j, i][0] = hsvImage[j, i - 1][0]
                hsvImage[j, i][1] = hsvImage[j, i - 1][1]
                hsvImage[j, i][2] = hsvImage[j, i - 1][2]
                #hsvi[j, i][1] = (int(hsvi[j, i][1]) + int(hsvi[j, i - 1][1])) / 2
                #hsvi[j, i][2] = (int(hsvi[j, i][2]) + int(hsvi[j, i - 1][2])) / 2
            '''
            elif i + 1 < width and isWaterMark(hsvi, j, i, j, i + 1):
                hsvi[j, i][1] = hsvi[j, i+1][1]
                hsvi[j, i][2] = hsvi[j, i+1][2]
        '''

    cv.imshow("water", hsvImage[:, :, 2])

    mask5 = hsvImage[:, :, 2]
    mask55 = cv.inRange(mask5, lower, upper)
    cv.imshow("mask55", mask55)

    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(mask55, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    ## [hough_lines]
    #  Standard Hough Line Transform
    lines = cv.HoughLines(mask55, 1, np.pi / 180, 150, None, 0, 0)
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
    linesP = cv.HoughLinesP(mask55, 1, np.pi / 180, 20, None, 5, 10)
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
