import cv2
import numpy as np

# Define the window name
window_name = 'Color Calibration'

# Create a window
cv2.namedWindow(window_name)

# Create trackbars for color change
colors = ['red', 'blue', 'green', 'yellow']
for color in colors:
    cv2.createTrackbar(f'{color}_low_H', window_name, 0, 179, lambda x: None)
    cv2.createTrackbar(f'{color}_high_H', window_name, 179, 179, lambda x: None)
    cv2.createTrackbar(f'{color}_low_S', window_name, 0, 255, lambda x: None)
    cv2.createTrackbar(f'{color}_high_S', window_name, 255, 255, lambda x: None)
    cv2.createTrackbar(f'{color}_low_V', window_name, 0, 255, lambda x: None)
    cv2.createTrackbar(f'{color}_high_V', window_name, 255, 255, lambda x: None)

# Initialize the video capture object for the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was successfully captured
    if ret:
        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get the current positions of the trackbars
        for color in colors:
            low_H = cv2.getTrackbarPos(f'{color}_low_H', window_name)
            high_H = cv2.getTrackbarPos(f'{color}_high_H', window_name)
            low_S = cv2.getTrackbarPos(f'{color}_low_S', window_name)
            high_S = cv2.getTrackbarPos(f'{color}_high_S', window_name)
            low_V = cv2.getTrackbarPos(f'{color}_low_V', window_name)
            high_V = cv2.getTrackbarPos(f'{color}_high_V', window_name)

            # Create a mask for the current color
            lower = np.array([low_H, low_S, low_V], dtype=np.uint8)
            upper = np.array([high_H, high_S, high_V], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame, frame, mask=mask)

            # Display the resulting frame
            cv2.imshow(f'{color}', res)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
