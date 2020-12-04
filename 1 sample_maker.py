from PIL import ImageGrab
import cv2
import numpy as np
import time

while True:

    #We grab an image of the screen with ImageGrab and then convert it
    # into numpy array so opencv can manipulate it
    img = ImageGrab.grab()
    img = np.array(img)

    #In case you don't have a dual monitor setup replace following line
    # with the comment on the right, since opencv only detect key input
    # if you have a focus on it's window
    img2 = img #img2 = img[100:150,100:250]
    cv2.imshow("Image", img2)
    
    #We save the return from waitKey in order to check for the following keys
    # we add timestamp at the end so all image names are unique
    key = cv2.waitKey(1)
    # the program will quit if we press q
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    # if we press p, it will save captured image to folder of positive samples
    if key == ord('p'):
        cv2.imwrite("Pos/img{}.png".format(time.time()),img)
    # if we press n, it will save captured image to folder of negative samples
    if key == ord('n'):
        cv2.imwrite("Neg/img{}.png".format(time.time()),img)
