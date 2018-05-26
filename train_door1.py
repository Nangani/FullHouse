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

svm = cv.ml.SVM_create()
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setType(cv.ml.SVM_C_SVC)
#svm.setC(100)
#svm.setGamma(5.383)

hog = get_hog()

trainTemp = []
responseTemp = []

#door
for i in range(1, 200):
    a = 'training/door/door' + str(i) + '.png'
    img = cv.imread(a, 0)
    if img is None:
        a=1
    else:
        train_cells = cv.resize(img, (36, 44))
        trainTemp.append(hog.compute(train_cells))
        responseTemp.append(0)

#not door
for i in range(1, 1299):
    a = 'training/notdoor/notdoor' + str(i) + '.png'
    img = cv.imread(a, 0)
    if img is None:
        a=1
    else:
        train_cells = cv.resize(img, (36, 44))
        trainTemp.append(hog.compute(train_cells))
        responseTemp.append(1)

trainData = np.array(trainTemp)
responses = np.array(responseTemp)
svm.train(trainData, cv.ml.ROW_SAMPLE, responses)
svm.save('svm_data.dat')