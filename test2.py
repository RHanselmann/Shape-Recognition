import numpy as np
import cv2
import matplotlib.pyplot as plt


path = r'D:\Unterlagen Studium\Python\Shape-Recognition\Shape-Recognition\sample_image.jpg'

img = cv2.imread(path)

# Get contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)
contours,h = cv2.findContours(thresh,1,2)

cv2.imshow('img1',thresh)

for cnt in contours:
	# compute the center of the contour
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    #print("x, y: ", cX, cY)

    # color detection (red, green, blue, yellow, violet)
    color = img[cY, cX+20];   #X and Y are swapped!!!!!!!!!!
    print(color)

    
    if color[0]>color[1] and color[0]>color[2]:
        if color[1]<200 and color[2]<100:
            print("blue")
            cv2.putText(img, "blue", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        elif color[1]<=color[2]:
            print("violet")
            cv2.putText(img, "violet", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            print("cyan")
            cv2.putText(img, "cyan", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
    elif color[1]>color[0] and color[1]>color[2]:
        print("green")
        cv2.putText(img, "green", (cX-20, cY-20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    elif color[2]>color[0] and color[2]>color[1]:
        if color[1]<100 and color[0]<100:
            print("red")
            cv2.putText(img, "red", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        elif color[1]<=color[0]:
            print("pink")
            cv2.putText(img, "pink", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            print("yellow")
            cv2.putText(img, "yellow", (cX-20, cY-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    


	# draw the contour and center of the shape on the image
    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 2, (255, 255, 255), -1)
    #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2

    # find shapes
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx) > 15:
        cv2.putText(img, "circle", (cX-20, cY+20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx)==4:
        cv2.minAreaRect(approx) 
        if True:
            cv2.putText(img, "square", (cX-20, cY+20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            cv2.putText(img, "rectangle", (cX-20, cY+20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    elif len(approx)==3:
        cv2.putText(img, "triangle", (cX-20, cY+20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


	# show the image
    cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#413 678
#701 558
#487 391
#182 343
#616 196