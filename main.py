__author__ = "Roman Hanselmann"
#__copyright__ = "-
#__credits__ = ["-"]
#__license__ = "-"
#__version__ = "1.0.1"
__maintainer__ = "Roman Hanselmann"
__email__ = "roman.hanselmann@stud.fhgr.ch"
__status__ = "Development"


#### Imports
import numpy as np
import cv2
import platform
import matplotlib.pyplot as plt
  

#### Variables
DEVICE_ID = 0       #change here, to open your preferred webcam 

# Select mode
mode = "cam"        #"cam" for a live video from your cam (change Device ID)
#mode = "image"      #"image" to load and show an image (change path)

# Path to image
path = r'D:\Unterlagen Studium\Python\Shape-Recognition\Shape-Recognition\sample_image.jpg'


def init_cam():
    if platform.system() == 'Windows':
        videoBackend = cv2.CAP_DSHOW
    else:
        videoBackend = cv2.CAP_ANY
            
    cap = cv2.VideoCapture(DEVICE_ID, videoBackend)
      
    if not cap.isOpened():
        print('ERROR: could not open webcam')
    
    return cap


def main():
    if(mode == "cam"):
        cap = init_cam()
            
        while(True):
            ret, img = cap.read()
            if not ret:
                print('ERROR: could not read data from webcam')
                break
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)

            cv2.imshow("'Q' - quit     \n'S' - settings", img)
            cv2.imshow("Binary", thresh)

            # Wait till a key is pressed
            ch = cv2.waitKey(10)
            if ch == ord('q'):
                break
            if ch == ord('s'):
                cap.set(cv2.CAP_PROP_SETTINGS,0)

        img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21) #reduce noise

        cap.release()
        cv2.destroyAllWindows()
    
    elif(mode == "image"):
        # Reading an image in default mode
        img = cv2.imread(path)       
        cv2.imshow("Image", img)

        # waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0)

    # Get contours
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)
    contours,h = cv2.findContours(thresh,1,2)
    cv2.imshow("Binary", thresh)

    # Edit image
    for cnt in contours:
        # compute the center of the contour
        M = cv2.moments(cnt)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #print("x, y: ", cX, cY)

        except ZeroDivisionError:
            print('Cannot devide by zero.')

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
        #cv2.circle(img, (cX, cY), 2, (255, 255, 255), -1)      #mark the center of the contour

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

    
if __name__ == "__main__":
    main()