import cv2 as cv
import numpy as np

filename = "plan.png"

src = cv.imread(filename, cv.IMREAD_COLOR)
hsvImage = cv.cvtColor(src, cv.COLOR_BGR2HSV)

lower = np.array([[[0, 0, 0]]])
upper = np.array([[[180, 255, 30]]])
mask = cv.inRange(hsvImage, lower, upper)
aaa = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

cv.imwrite('temp.png', aaa)
