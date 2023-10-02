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
  

#### Variables
DEVICE_ID = 0       #change here, to open your preferred webcam 

# Select mode
mode = "cam"        #"cam" for a live video from your cam (change Device ID)
#mode = "image"      #"image" to load and show an image (change path)

# Path to image
path = r'D:\Unterlagen Studium\Python\Shape-Recognition\Shape-Recognition\sample_image.jpg'




def main():
    if(mode == "cam"):
        if platform.system() == 'Windows':
            videoBackend = cv2.CAP_DSHOW
        else:
            videoBackend = cv2.CAP_ANY
            
        cap = cv2.VideoCapture(DEVICE_ID, videoBackend);
        
        if not cap.isOpened():
            print('ERROR: could not open webcam');
            
        while(True):
            ret, frame = cap.read();
            if not ret:
                print('ERROR: could not read data from webcam')
                break;
            
            cv2.imshow("Press 'q' to quit.", frame)
            ch = cv2.waitKey(20);
            if ch==ord('q'):
                break;
            if ch==ord('0'):
                cap.set(cv2.CAP_PROP_SETTINGS,0);

        cap.release();
        cv2.destroyAllWindows();
    
    elif(mode == "image"):
        # Reading an image in default mode
        image = cv2.imread(path)
        
        # Window name in which the image is displayed
        window_name = 'image'
        
        # Using cv2.imshow() method
        # Displaying the image
        cv2.imshow(window_name, image)

        # waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0)


    
if __name__ == "__main__":
    main();