import cv2
from ultralytics import YOLO,checks
import math
import time
from outlet import outlt
import sys
import detect

print()
print(f"""

$$\     $$\  $$$$$$\  $$\       $$$$$$\           $$$$$$\  $$$$$$$\  $$\      $$\         _
\$$\   $$  |$$  __$$\ $$ |     $$  __$$\         $$  __$$\ $$  __$$\ $$$\    $$$ |      /( )\  
 \$$\ $$  / $$ /  $$ |$$ |     $$ /  $$ |        $$ /  $$ |$$ |  $$ |$$$$\  $$$$ |     / / \ \    __
  \$$$$  /  $$ |  $$ |$$ |     $$ |  $$ |$$$$$$\ $$$$$$$$ |$$$$$$$  |$$\$$\$$ $$ |    / /   \ \_ / _\  
   \$$  /   $$ |  $$ |$$ |     $$ |  $$ |\______|$$  __$$ |$$  __$$< $$ \$$$  $$ |   / /     \__O (__
    $$ |    $$ |  $$ |$$ |     $$ |  $$ |        $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |  / /___       \__/  
    $$ |     $$$$$$  |$$$$$$$$\ $$$$$$  |        $$ |  $$ |$$ |  $$ |$$ | \_/ $$ | |YOLO  |
    \__|     \______/ \________|\______/         \__|  \__|\__|  \__|\__|     \__| |___ARM|       -Gokul
{sys.version},{checks()}
""")

class main:

    def __inti__(self):
        print("Hello world")
        model = YOLO("rr.pt")
        classNames = ["ball", "battery", "grip"]
    def detect(self,frame,cap):
        detect.detector(frame,cap)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)  # Adjust the height to 480 for a 16:9 aspect ratio
main()
while True:
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
                main.detect(frame=img,cap=cap)
                
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            confidence = math.ceil((box.conf[0]*100))/100
            text = f"{class_name} ({confidence})"
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
 



    # Display the image with bounding boxes
    cv2.imshow('Webcam', img)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
      