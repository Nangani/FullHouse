"""
@file hough_lines.py
@brief This program demonstrates line finding with the Hough transform
"""

import cv2 as cv
import numpy as np

filename = "plan.png"

# Loads an image
src = cv.imread(filename, cv.IMREAD_COLOR)
hsvImage = cv.cvtColor(src, cv.COLOR_BGR2HSV)
#    cv.imshow("hsvImage", hsvImage)
lower = np.array([[[0, 0, 0]]])
upper = np.array([[[180, 255, 30]]])
mask = cv.inRange(hsvImage, lower, upper)
aaa = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

#   cv.imshow("mask", mask)
cv.imwrite('temp.png', aaa)
height = np.size(src, 0)
width = np.size(src, 1)

#print(width)
#print(height)

#print(src[height-1][width-1])

#  cv.imshow("water", hsvImage[:, :, 2])

mask5 = hsvImage[:, :, 2]
mask55 = cv.inRange(mask5, lower, upper)
# cv.imshow("mask55", mask55)

# Copy edges to the images that will display the results in BGR
cdst = cv.cvtColor(mask55, cv.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)

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
#    ## [imshow]
# Show results
#   cv.imshow("Source", src)
#  cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
# cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
## [imshow]
## [exit]
# Wait and Exit
## [exit]