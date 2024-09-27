import cv2 as cv

class Camera:
    
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera")
        
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
            
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return (ret, cv.ctrColor(frame, cv.COLOR_BGR2RGB))
            else:
                raise ValueError("Unable to capture frame from the camera")
        else:
            return None