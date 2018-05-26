import cv2 as cv
import numpy as np

def get_hog() :
    winSize = (36,44)
    blockSize = (18,22)
    blockStride = (9,11)
    cellSize = (9,11)
    nbins = 9
    derivAperture = 1
    winSigma = -1.
    histogramNormType = 0
    L2HysThreshold = 0.2
    gammaCorrection = 1
    nlevels = 64
    signedGradient = False

    hog = cv.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradient)

    return hog

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

img = cv.imread('test/test2.png', 0)

hog = get_hog()
svm = cv.ml.SVM_load('svm_data.dat')
svmvec = svm.getSupportVectors()[0]
rho = -svm.getDecisionFunction(0)[0]
svmvec = np.append(svmvec, rho)
hog.setSVMDetector(svmvec)
hogParams = { 'finalThreshold': 1}
#found, w = hog.detect(img)
#found, w = hog.detectMultiScale(img, **hogParams)
found, w = hog.detectMultiScale(img)
print(found)
print(w)
found_filtered = []
'''
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and inside(r, q):
            break
        else:
            found_filtered.append(r)
draw_detections(img, found_filtered, 3)
'''
draw_detections(img, found)



#print(found_filtered)
# display image

cv.imshow('asdf', img)

cv.waitKey(0)
