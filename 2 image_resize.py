import os
import numpy
import cv2

#first we specify the folder that the images are in
folder = "Pos"

#next we get the list of all the names of the images
img_list = os.listdir(folder)

#we loop throug all names and read the image, resize it and save
# it in a new folder. In my case I just added "S" for Smaller
for name in img_list:
    img = cv2.imread(folder+"/"+name)
    img = cv2.resize(img,(600,300))
    cv2.imwrite(folder+"S/"+name,img)