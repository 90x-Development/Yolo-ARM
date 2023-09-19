import cv2
import numpy as np

# Open the webcam (you can specify the camera index, typically 0 for the built-in webcam)
cap = cv2.VideoCapture(0)

# Set the desired resolution (614x614 in this case)
cap.set(3, 614)  # Width
cap.set(4, 614)  # Height

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break
    frame = frame[100:380,140:500]
    # Draw sample lines on the frame
    cv2.line(frame, (50, 0), (50, 500), (0, 255, 0), 2)
    cv2.line(frame, (0, 140), (639, 140), (0, 0, 255), 2)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Video resolution: {width}x{height}")
    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
