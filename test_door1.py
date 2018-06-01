import cv2 as cv
import numpy as np

def get_hog1() :
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

def get_hog2() :
    winSize = (44,36)
    blockSize = (22,18)
    blockStride = (11,9)
    cellSize = (11,9)
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


import numpy as np


# Malisiewicz et al.
def non_max_suppression_fast(boxes, overlapThresh):
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
        return []

    # if the bounding boxes integers, convert them to floats --
    # this is important since we'll be doing a bunch of divisions

    if boxes.dtype.kind == "i":

        boxes = boxes.astype("float")

    # initialize the list of picked indexes
    pick = []

    # grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    # compute the area of the bounding boxes and sort the bounding
    # boxes by the bottom-right y-coordinate of the bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    # keep looping while some indexes still remain in the indexes
    # list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the
        # index value to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # find the largest (x, y) coordinates for the start of
        # the bounding box and the smallest (x, y) coordinates
        # for the end of the bounding box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]

        # delete all indexes from the index list that have
        idxs = np.delete(idxs, np.concatenate(([last],
                                               np.where(overlap > overlapThresh)[0])))

    # return only the bounding boxes that were picked using the
    # integer data type
    return boxes[pick].astype("int")

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

def findDoor():
    img = cv.imread('plan.png', 0)
    hog1 = get_hog1()
    hog2 = get_hog2()

    #door1
    svm = cv.ml.SVM_load('svm_door1.dat')
    svmvec = svm.getSupportVectors()[0]
    rho = -svm.getDecisionFunction(0)[0]
    svmvec = np.append(svmvec, rho)
    hog1.setSVMDetector(svmvec)
    hogParams = { 'finalThreshold': 1}
    #found, w = hog.detect(img)
    #found, w = hog.detectMultiScale(img, **hogParams)
    found1, w1 = hog1.detectMultiScale(img)

    #door2
    svm = cv.ml.SVM_load('svm_door2.dat')
    svmvec = svm.getSupportVectors()[0]
    rho = -svm.getDecisionFunction(0)[0]
    svmvec = np.append(svmvec, rho)
    hog2.setSVMDetector(svmvec)
    found2, w2 = hog2.detectMultiScale(img)

    # door3
    svm = cv.ml.SVM_load('svm_door3.dat')
    svmvec = svm.getSupportVectors()[0]
    rho = -svm.getDecisionFunction(0)[0]
    svmvec = np.append(svmvec, rho)
    hog1.setSVMDetector(svmvec)
    found3, w3 = hog1.detectMultiScale(img)

    # door4
    svm = cv.ml.SVM_load('svm_door4.dat')
    svmvec = svm.getSupportVectors()[0]
    rho = -svm.getDecisionFunction(0)[0]
    svmvec = np.append(svmvec, rho)
    hog2.setSVMDetector(svmvec)
    found4, w4 = hog2.detectMultiScale(img)

    found = []
    for i in range(0, len(found1)):
        if found1[i][2] + found1[i][3] <= 120 and w1[i] >= 0.2:
            found.append(found1[i])
    for i in range(0, len(found2)):
        if found2[i][2] + found2[i][3] <= 120 and w2[i] >= 0.2:
            found.append(found2[i])
    for i in range(0, len(found3)):
        if found3[i][2] + found3[i][3] <= 120 and w3[i] >= 0.2:
            found.append(found3[i])
    for i in range(0, len(found4)):
        if found4[i][2] + found4[i][3] <= 120 and w4[i] >= 0.2:
            found.append(found4[i])

    #draw_detections(img, found, 1)
    #found_filtered = non_max_suppression_fast(np.array(found), 0.25)
    draw_detections(img, found, 1)

    #cv.imshow('asdf', img)
    #cv.waitKey(0)

    return found

#if __name__ == '__main__':
#    findDoor()