from PIL import Image,ImageFilter

image = Image.open("sample.png")
px = image.load()
vertex = []
wallStart = []
wallEnd = []
wall = []
untilStop =0
(width,height) = image.size
coordinate = [[0 for col in range(width)] for row in range(height)]
print(image.size)
for i in range(0,height-1):
    for j in range(0,width-1):
        if(px[j,i] == (255,255,255)):
            coordinate[i][j] = 1

"""
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
"""

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


print(vertex)
#print(wallEnd)
#for row in coordinate:
#        print (row)