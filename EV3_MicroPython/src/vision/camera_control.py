import cv2 
import numpy as np

# Open a handle to the USB camera
#choosing index 1 because we use a laptop with an external usb camera , that's why we choose the second camera 

def open_camera(camera_index=0): 
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"No camera found at index {camera_index}- please reconnect your USB-camera")
        return None
    return cap
        
        
# if you have other cameras 
# Attempt to open the first few indices. This can be deleted it just checks if there are multiple cameras and choose the active one 
'''
 for index in range(0, 4):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"No camera found at index {index}")
        cap.release()
        continue
    else:
        ret, frame = cap.read()
        if ret:
            cv2.imshow(f"Test Frame from Camera Index {index}", frame)
            cv2.waitKey(1000)  # Display each frame for 1000 milliseconds
            print(f"Camera found at index {index}")
        cap.release()

cv2.destroyAllWindows() 
'''
class DetectedCircles:
    def __init__(self,x,y, radius):
        self.x=x
        self.y = y
        self.radius = radius
        
    
    
def detect(cap):
 balls_list = [] # List to store the deteced balls 
 while True:
    # Capturing frames
    ret, frame = cap.read()
    if not ret:
        break
    
    #dimensions
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # Convert to grayscale for thresholding and circle detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9,9),0) 
    _, thresholded = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)

    # Detect circles using Hough Circles white Balls 
    circles = cv2.HoughCircles(thresholded, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                param1=50, param2=30, minRadius=0, maxRadius=0)
                                
    #Detect orange Balls                             
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower_orange = np.array([5, 50, 50])
    #upper_orange = np.array([15, 255, 255])
    #mask = cv2.inRange(hsv, lower_orange, upper_orange)
    #circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
    #                          param1=50, param2=30, minRadius=0, maxRadius=0)
    
    
    
    # Draw circles on the original frame - UI for detection 
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(frame,(i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            circle_details = DetectedCircles(i[0], i[1], i[2])
            balls_list.append(circle_details)
            
            
            
    # Display and Detect
    cv2.imshow('Frame with Detected Objects - Ball-obstacles-', frame)
    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    # When everything done, release the capture and destroy all windows
    #cap.release()
    #cv2.destroyAllWindows()
    return balls_list
    
 
 

def main():
    """ Main function to control the camera and detect objects (balls-obstacles and the field)""" 
    cap = open_camera()
    if cap is not None:
        detect(cap)
if __name__ == "__main__":
 main()