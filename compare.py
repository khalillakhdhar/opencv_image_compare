import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image1 = cv2.imread("banana.jpg")
image2 = cv2.imread("logo.jpg")
grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayImage = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
dim = (200, 200)

image1 = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
image2 = cv2.resize(image2, dim, interpolation = cv2.INTER_AREA)

difference = cv2.subtract(image1, image2)

result = not np.any(difference) #if difference is all zeros it will return False
print(difference)
file2write=open("texte.txt",'w')
for i in range(len(difference)):
    # parcourir les colonnes
    for j in range(len(difference[0])):
        file2write.write(str(difference[i][j]))
file2write.close()
if result is True:
    print("The images are the same")
else:
    cv2.imwrite("result.jpg", difference)
    print("the images are different")
img=mpimg.imread('result.jpg')
imgplot = plt.imshow(img)
plt.show()