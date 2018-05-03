from PIL import Image


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
for i in range(0, height - 1):
    for j in range(0, width - 1):
        if (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 1 and coordinate[i + 1][j - 1] == 1 and coordinate[i][j + 1] == 0 and coordinate[i + 1][j] == 0 and coordinate[i + 1][j + 1] == 0)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i - 1][j] == 1 and coordinate[i - 1][j + 1] == 1 and coordinate[i][j] == 1 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j + 1] == 1 and coordinate[i][j - 1] == 0 and coordinate[i + 1][j - 1] == 0 and coordinate[i + 1][j] == 0)\
                or (coordinate[i - 1][j + 1] == 1 and coordinate[i][j] == 1 and coordinate[i][j + 1] == 1 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1 and coordinate[i - 1][j - 1] == 0 and coordinate[i - 1][j] == 0 and coordinate[i][j - 1] == 0)\
                or (coordinate[i - 1][j - 1] == 1 and coordinate[i][j - 1] == 1 and coordinate[i][j] == 1 and coordinate[i + 1][j - 1] == 1 and coordinate[i + 1][j] == 1 and coordinate[i + 1][j + 1] == 1 and coordinate[i - 1][j] == 0 and coordinate[i - 1][j + 1] == 0 and coordinate[i][j + 1] == 0):
            coordinate[i][j] = 0
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

print(coordinate)
