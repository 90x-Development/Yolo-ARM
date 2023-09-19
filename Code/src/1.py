import cv2
from ultralytics import YOLO
import math
import time

model = YOLO("rr.pt")
classNames = ["ball", "battery", "grip"]

# Open the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480) 

def detector(frame,cap):
    img = cap.read()
    results=model(img)
    battery_found = False

    results = model(img)
    for r in results:
        boxes = r.boxes

        for box in boxes:
 
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
   
            

            class_name = classNames[int(box.cls[0])]
            if class_name=="battery":
                battery_found=True
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                battery_center = (cx, cy)
                print(f"Battery found at coordinates (x1, y1): ({x1}, {y1}), (x2, y2): ({x2}, {y2})")
                cv2.rectangle(img,battery_center,battery_center (255, 165, 0), 3)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 165, 0), 1)
                confidence = math.ceil((box.conf[0] * 100)) / 100
                text = f"{class_name} ({confidence})"
                cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                return cx,cy
                
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            confidence = math.ceil((box.conf[0]*100))/100
            text = f"{class_name} ({confidence})"
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
 




