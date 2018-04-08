from PIL import Image


image = Image.open("sample.png")
px = image.load()
(width, height) = image.size
coordinate = [[0 for col in range(width)] for row in range(height)]

for i in range(0,height-1):
    for j in range(0,width-1):
        if px[j,i] >= (220,220,220):
            coordinate[i][j] = 1

print(coordinate)