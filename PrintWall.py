from PIL import Image
import cv2 as cv
import numpy as np
import test_door1

image = Image.open("temp.png")
px = image.load()
(width, height) = image.size
coordinate = [[0 for col in range(width)] for row in range(height)]

for i in range(0,height-1):
    for j in range(0,width-1):
        if px[j,i] >= (220,220,220):
            coordinate[i][j] = 1
for i in range(0,height-1):
    for j in range(0,width-1):
        if(coordinate[i][j]*4+coordinate[i][j+1]*2+coordinate[i+1][j]*2+coordinate[i-1][j]*2+coordinate[i][j-1]*2+coordinate[i+1][j+1]*1+coordinate[i-1][j+1]*1+coordinate[i+1][j-1]*1+coordinate[i-1][j-1]*1<9):
            coordinate[i][j]=0

"""
111  111  001  100
110  011  011  110
100  001  111  111
"""
"""
000  110  111  011
10   100  10   001
111  1 0  000  0 1
"""
for i in range(0, height - 1):
    for j in range(0, width - 1):
        if (coordinate[i][j] == 0 and coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1 and coordinate[i][j - 1] == 1)\
                or (coordinate[i][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j + 1] == 0 and coordinate[i + 1][j + 1] == 0 and coordinate[i - 1][j - 1] == 1 and coordinate[i][j - 1] == 1 and coordinate[i + 1][j - 1] == 1 and coordinate[i - 1][j] == 1)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 0 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 0 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j - 1] == 0 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j + 1] == 1):
            coordinate[i][j] = 1
"""
0 1  1 0  111  000
001  100   01   01
011  110  000  111
"""

for i in range(height - 2, 0, -1):
    for j in range(width - 2, 0, -1):
        if (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j - 1] == 0 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 0 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 0 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1):
            coordinate[i][j] = 1
"""
000  110  011  000
100  100  001  001
110  000  000  011
"""
for i in range(0, height - 1):
    for j in range(0, width - 1):
        if (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 0 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 0 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 0 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j - 1] == 0 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 0 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j - 1] == 0 and coordinate[i][j] == 0 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1):
            coordinate[i][j] = 1

for i in range(0,height-1):
    for j in range(0,width-1):
        if(coordinate[i][j]*4+coordinate[i][j+1]*2+coordinate[i+1][j]*2+coordinate[i-1][j]*2+coordinate[i][j-1]*2+coordinate[i+1][j+1]*1+coordinate[i-1][j+1]*1+coordinate[i+1][j-1]*1+coordinate[i-1][j-1]*1<9):
            coordinate[i][j]=0
        else:
            coordinate[i][j] = 1

xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]
check = [[0 for col in range(width)] for row in range(height)]
for i in range(0, height):
    for j in range(0, width):
        if coordinate[i][j] == 1 and check[i][j] == 0:
            check[i][j] = 1
            queue_x = []
            queue_y = []
            queue_x.append(i)
            queue_y.append(j)
            cnt = 1

            while len(queue_x) > 0:
                for k in range(0, 4):
                    if coordinate[queue_x[0] + xx[k]][queue_y[0] + yy[k]] == 1 and check[queue_x[0] + xx[k]][queue_y[0] + yy[k]] == 0:
                        check[queue_x[0] + xx[k]][queue_y[0] + yy[k]] = 1
                        queue_x.append(queue_x[0] + xx[k])
                        queue_y.append(queue_y[0] + yy[k])
                        cnt += 1
                queue_x.pop(0)
                queue_y.pop(0)

            if cnt < 40:
                coordinate[i][j] = 0
                check[i][j] = 2
                queue_x = []
                queue_y = []
                queue_x.append(i)
                queue_y.append(j)
                while len(queue_x) > 0:
                    for k in range(0, 4):
                        if coordinate[queue_x[0] + xx[k]][queue_y[0] + yy[k]] == 1 and check[queue_x[0] + xx[k]][queue_y[0] + yy[k]] == 1:
                            check[queue_x[0] + xx[k]][queue_y[0] + yy[k]] = 2
                            coordinate[queue_x[0] + xx[k]][queue_y[0] + yy[k]] = 0
                            queue_x.append(queue_x[0] + xx[k])
                            queue_y.append(queue_y[0] + yy[k])
                    queue_x.pop(0)
                    queue_y.pop(0)

door = test_door1.findDoor()
flag = 0

for k in range(0, len(door)):
    start_x = door[k][1]
    start_y = door[k][0]
    len_x = door[k][3]
    len_y = door[k][2]
    x = int(start_x + (len_x / 2))
    y = int(start_y + (len_y / 2))
    flag = 0
    if len_x > len_y:
        for j in range(10, 30):
            if flag == 1:
                break
            for i in range(start_x - 5, start_x + len_x + 5):
                if i >= height or y - j < 0 or y + j >= width:
                    break
                if coordinate[i][y - j] == 1 and coordinate[i][y + j] == 1:
                    for jj in range(y - j, y + j + 1):
                        if coordinate[i][jj] != 1:
                            coordinate[i][jj] = 2
                    flag = 1
    else:
        for i in range(10, 40):
            if flag == 1:
                break
            for j in range(start_y - 5, start_y + len_y + 5):
                if j >= width or x - i < 0 or x + i >= height:
                    break
                if coordinate[x - i][j] == 1 and coordinate[x + i][j] == 1:
                    for ii in range(x - i, x + i + 1):
                        if coordinate[ii][j] != 1:
                            coordinate[ii][j] = 2
                    flag = 1

f = open('ww.txt', 'w')
f.write(str(coordinate))
