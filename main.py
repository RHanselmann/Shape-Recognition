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
#mode = "cam"        #"cam" for a live video from your cam (change Device ID)
mode = "image"      #"image" to load and show an image (change path)

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

def get_color(img, cX, cY):
    # color detection (red, green, blue, yellow, violet)
    color = img[cY, cX+20];   #X and Y are swapped!!!!!!!!!!
    color_str = "unknown"
    #print("color value: ", color)

    if color[0]>color[1] and color[0]>color[2]:
        if color[1]<200 and color[2]<100:
            color_str = "blue"
        elif color[1]<=color[2]:
            color_str = "violet"
        else:
            color_str = "cyan"
            
    elif color[1]>color[0] and color[1]>color[2]:
        color_str = "green"
    elif color[2]>color[0] and color[2]>color[1]:
        if color[1]<100 and color[0]<100:
            color_str = "red"
        elif color[1]<=color[0]:
            color_str = "pink"
        else:
            color_str = "yellow"
    
    return color_str
     
def get_shape(img, cX, cY, cnt):
    shape_str = "unknown"
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx) > 15:
        shape_str = "circle"
    elif len(approx)==4:
        cv2.minAreaRect(approx) 
        if True:        #differentiat between square and rectangle. to do!!!!!!
            shape_str = "square"
        else:
            shape_str = "rectangle"
    elif len(approx)==3:
        shape_str = "triangle"

    return shape_str

def get_contour_center(cnt):
    # compute the center of the contour
    M = cv2.moments(cnt)
    try:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #print("contour center: ", cX, cY)

    except ZeroDivisionError:
        print('Cannot devide by zero.')

    return cX, cY

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

    # Get contours
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)
    contours,h = cv2.findContours(thresh,1,2)
    cv2.imshow("Binary", thresh)

    # Edit image
    for cnt in contours:
        cX, cY = get_contour_center(cnt)

        # Colors
        color_str = get_color(img, cX, cY)
        print(color_str)
        cv2.putText(img, color_str, (cX-20, cY-20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)  # -20 is there to put the text a bit higher

        # draw the contour and center of the shape on the image
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
        #cv2.circle(img, (cX, cY), 2, (255, 255, 255), -1)      #mark the center of the contour

        # Shapes
        shape_str = get_shape(img, cX, cY, cnt)
        cv2.putText(img, shape_str, (cX-20, cY+20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


	# show the image
    cv2.imshow("Image", img)
    
    cv2.waitKey(0)

    
if __name__ == "__main__":
    main()