import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_contours(img):
    # Get contours
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)
    contours,h = cv2.findContours(thresh,1,2)

    return contours




path = r'D:\Unterlagen Studium\Python\Shape-Recognition\Shape-Recognition\sample_image.jpg'

img = cv2.imread(path)

# Get contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)
contours,h = cv2.findContours(thresh,1,2)

cv2.imshow('img1',thresh)

cv2.waitKey(0)

for cnt in contours:
	# compute the center of the contour
	M = cv2.moments(cnt)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
	cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(img, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	# show the image
	cv2.imshow("Image", img)
	cv2.waitKey(0)
     
cv2.waitKey(0)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    #print len(approx)
    if len(approx) > 15:
        print('circle')
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        cv2.minAreaRect(approx) 
        if True:
            print('square')
            cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        else:
            print('rectangle')
            cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==3:
        print('triangle')
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)

    cv2.imshow('img3',img)
    cv2.waitKey(0)
        

cv2.destroyAllWindows()
