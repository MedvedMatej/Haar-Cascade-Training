from PIL import ImageGrab
import cv2
import numpy as np
import time

#Load cascade
cascade = cv2.CascadeClassifier('Training/cascade.xml')

def draw_rectangles(haystack_img, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv2.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv2.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)

        return haystack_img

while True:
    #Grab screen image and conver it to numpy array
    img = ImageGrab.grab()
    img = np.array(img)

    #we feed the image to our cascade and receive boundig box positions
    rect = cascade.detectMultiScale(img)

    #we change the colors so we can see it in RGB
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #drawing the rectangles on detected spots
    result = draw_rectangles(img,rect)

    #showing
    cv2.imshow('Result',img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

