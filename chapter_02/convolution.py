import imageio
import numpy as np
from skimage import img_as_ubyte

im = imageio.imread('baikinman.jpg')
print(im.shape)

#imageio.imwrite("foo.png", im)

yy = im.shape[0]
xx = im.shape[1]

filter1 = [ [1, 1, 1],
           [0, 0, 0],
           [-1, -1, -1]]


filter2 = [ [1, 1, 1],
           [0, 0, 0],
           [-1, -1, -1]]

sobel = [ [1, 2, 1],
           [0, 0, 0],
           [-1, -2, -1]]

filtered_image = []
for y in range(0,yy-3):
    row = []
    for x in range(0,xx-3):
        val = 0.0
        for i in range(0,3):
            for j in range(0,3):
                val += im[y+i, x+j] * filter1[i][j]
        row.append(val)
    filtered_image.append(row)

"""
img = np.array(filtered_image)
mn = np.min(img)

print(mn)

if(mn < 0):
    img += (-mn)

print(np.max(img))

mx = np.max(img)
print(mx)
img1 = ((np.array(img) / mx) * 255.).astype(np.uint8)
img1[img1 >= 110] = 0

"""
img1 = np.array(filtered_image)


imageio.imwrite("baikinman_filter_no_thresh.png", img1)