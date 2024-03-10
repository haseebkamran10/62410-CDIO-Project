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
class DetectedRobot:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h        
        
    
    
def detect(cap, robot_template):
 balls_list = [] # List to store the deteced balls 
 robot_position = None 
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
    edges = cv2.Canny(blurred, 50, 150)
    #_, thresholded = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)

    # Detect circles using Hough Circles white Balls 
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                param1=50, param2=30, minRadius=30, maxRadius=50)
    # Draw circles on the original frame - UI for detection 
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(frame,(i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            circle_text = f"({i[0]}, {i[1]}), Radius: {i[2]}"
            text_position = (i[0] - i[2], i[1] + i[2] + 10)
            cv2.putText(frame, circle_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, (0, 0, 255), 1, cv2.LINE_AA)
            balls_list.append(DetectedCircles(i[0], i[1], i[2]))
    
    #Robot detection using the template matching- maybe we have to use another method in the future 
    for scale in np.linspace(0.5, 1.5, 20):  # Example: scales from 0.5x to 1.5x original size
            resized_template = cv2.resize(robot_template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_template = cv2.cvtColor(resized_template, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(gray_frame, gray_template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            if loc[0].size > 0:  # If there are matches at this scale
                pt = loc[1][0], loc[0][0]  # Take the first match
                cv2.rectangle(frame, pt, (pt[0] + resized_template.shape[1], pt[1] + resized_template.shape[0]), (255, 0, 0), 2)
                robot_position = DetectedRobot(pt[0], pt[1], resized_template.shape[1], resized_template.shape[0])
                break  # Stop searching once we've found a match
                
            
            
            
    # Display and Detect
    cv2.imshow('Frame with Detected Objects-', frame)
    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    # When everything done, release the capture and destroy all windows
    #cap.release()
    #cv2.destroyAllWindows() 

 return balls_list, robot_position  
 
 

def main():
    """ Main function to control the camera and detect objects (balls-obstacles and the field)""" 
    cap = open_camera()
    robot_template = cv2.imread('C:\\Users\\fathi\\Documents\\GitHub\\62410-CDIO-Project\\EV3_MicroPython\\data\\images\\prototype.png') 
    if cap is not None and robot_template is not None:
        balls,robot = detect(cap, robot_template)
    print(f"Detected {len(balls)} balls.")
    for index,ball in enumerate(balls):
     print(f"Ball {index} at ({ball.x}, {ball.y}) with radius {ball.radius}.")
    if robot:
     print(f"Detected robot at ({robot.x}, {robot.y}).")
    else:
        print("No robot detected.")
 
   
        
if __name__ == "__main__":
 main()