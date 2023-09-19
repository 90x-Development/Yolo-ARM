import cv2,numpy

class Outlet:
    def __init__(self,cap):
        self.cap=cap

    def draw_outlet(self,frame):
        cv2.line(frame, (50, 0), (50, 500), (0, 255, 0), 2)
        cv2.line(frame, (0, 140), (639, 140), (0, 0, 255), 2) 
        return frame
       