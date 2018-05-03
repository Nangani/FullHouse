from PIL import Image
from PIL import ImageDraw
from area import area
import math

AA=0
AAAA =0
refvec = (0,1)
def centroid(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    _len = len(points)
    centroid_x = sum(x_coords)/_len
    centroid_y = sum(y_coords)/_len
    return [centroid_x, centroid_y]
def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector

image = Image.open("temp.png")
px = image.load()
vertex = []
wallStart = []
wallEnd = []
wall = []
(width, height) = image.size
sample = Image.new("RGB",(width,height))
draw = ImageDraw.Draw(sample)

coordinate = [[0 for col in range(width)] for row in range(height)]
for i in range(0,height-1):
    for j in range(0,width-1):
        if px[j,i] >= (220,220,220):
            coordinate[i][j] = 1

for i in range(0,height-1):
    for j in range(0,width-1):
        if(coordinate[i][j]*4+coordinate[i][j+1]*2+coordinate[i+1][j]*2+coordinate[i-1][j]*2+coordinate[i][j-1]*2+coordinate[i+1][j+1]*1+coordinate[i-1][j+1]*1+coordinate[i+1][j-1]*1+coordinate[i-1][j-1]*1<9):
            coordinate[i][j]=0
sample2 = Image.new("RGB",(width,height))
px2=sample2.load()
for i in range(0,height-1):
    for j in range(0,width-1):
        if(coordinate[i][j]==1):
            px2[j,i]=(0,255,255)

for i in range(0,height-1):
    for j in range(0,width-1):
        if (j in wall):
            continue
        if(coordinate[i][j] == 1):
            vertex.append((j, i))
            while(coordinate[i][j] == 1 and j not in wall):
                wall.append(j)
                j=j+1
            vertex.append((j-1, i))
wall.clear()

for i in range(height-1,0,-1):
    for j in range(width-1,0,-1):
        if (j in wall):
            continue
        if(coordinate[i][j] == 1):
            vertex.append((j, i))
            while(coordinate[i][j] == 1 and j not in wall):
                wall.append(j)
                j=j-1
            vertex.append((j-1, i))
wall.clear()
for i in range(0,width-1):
    for j in range(0,height-1):
        if (j in wall):
            continue
        if(coordinate[j][i] == 1):
            vertex.append((i, j))
            while(coordinate[j][i] == 1 and j not in wall):
                wall.append(j)
                j=j+1
            vertex.append((i, j-1))
wall.clear()
for i in range(width-1,0):
    for j in range(height-1,0):
        if (j in wall):
            continue
        if(coordinate[j][i] == 1):
            vertex.append((i, j))
            while(coordinate[j][i] == 1 and j not in wall):
                wall.append(j)
                j = j + 1
            vertex.append((i, j-1))
wall.clear()



origin = centroid(vertex)


vertex.sort(key=clockwiseangle_and_distance)
draw.polygon(vertex,fill=200)
px2 = sample.load()
for i in range(0,height-1):
	for j in range (0,width-1):
		if(px2[j,i]==(200,0,0)):
			coordinate[i][j]==1
sample.show()
size=len(vertex)
for i in range(0,size):
    j = (i+1)%size
    (x1,y1) = vertex[i]
    (x2,y2) = vertex[j]
    AAAA = AAAA+x1*y2
    AAAA = AAAA-y1*x2
print(coordinate)


#print(wallEnd)
#for row in coordinate:
#        print (row)
