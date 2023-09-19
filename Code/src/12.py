import cv2
from ultralytics import YOLO,checks
import math
import time
import angle
#
#from outlet import outlt
import sys
import detect
from threading import Thread
import time
import control
import simulate
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
#yes =input("PRESS ANY KEY")

def perform_object_detection():
    # Load the YOLO model
    model = YOLO("rr.pt")
    classNames = ["ball", "battery", "grip"]

    # Open the webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)  # Adjust the height to 480 for a 16:9 aspect ratio
    y =4
    while y > 3:
        success, img = cap.read()

        # Check if the frame was successfully captured
        if not success:
            print("Failed to capture frame")
            break
        img = img[100:380,140:500]
    # Draw sample lines on the frame

        # Perform object detection
        results = model(img)
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int values

                # Draw bounding box
                #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Display class name and confidence
                class_name = classNames[int(box.cls[0])]
                if class_name == "battery":
 
                    confidence = math.ceil((box.conf[0] * 100)) / 100 
                    if confidence>0.5:           
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0,165,255), 2) 
                        text = f"{class_name} ({confidence})"
                        cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2
                        cv2.line(img,(50,140),(cx,cy),(0,165,255),3,3)
                        bc=[cx,cy]
                        x=1
                        if y == 4:
                            Thread(target=arm ,args=(x,cx,cy)).start()
                            print("stared arm fun")
                            y=5
                    """   
                confidence = math.ceil((box.conf[0] * 100)) / 100
                text = f"{class_name} ({confidence})"
                cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                   """
        cv2.line(img, (50, 0), (50, 500), (0, 255, 0), 2)
        cv2.line(img, (0, 140), (639, 140), (0, 0, 255), 2) 
        # Display the image with bounding boxes
        cv2.imshow('Webcam', img)

        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()


def arm(x,cx,cy):
    time.sleep(3)

    ba=angle.calculate_angle(50,140,50,0,cx,cy)
    p = [50, 140]
    q = [cx, cy]

    vdist=math.dist(p, q)
    print (vdist)

    rdist=vdist/7#.40537210974
    print(f"found at {cx} {cy} at angle {ba} for distance {rdist}")
    print("============= 𝕀𝕟𝕚𝕥𝕚𝕒𝕝𝕚𝕫𝕚𝕟𝕘 PICK UP PROCESS =============")
    print(f"INITIATED picK uP a oBJECT aT x:{cx} y:{cy} \n distance :{vdist} /// {rdist} cm \n base angle is {ba}")

    simulate.plot_triangle(10,13,rdist)
if __name__ == '__main__':
    Thread(target=perform_object_detection).start()
