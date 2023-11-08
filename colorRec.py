import cv2
import numpy as np

# Define the target color matrix
target_matrix = np.array([
    [3, 1, 1, 1],
    [1, 1, 2, 2],
    [1, 1, 1, 1],
    [3, 1, 3, 1]
])

# Create a dictionary to map color numbers to color names
color_dict = {1: 'red', 2: 'blue', 3: 'yellow', 4: 'green'}

# Create a list to keep track of the positions that have been filled
filled_positions = []

# Initialize a counter for the number of blocks encountered
block_counter = 0

# Initialize a flag to indicate whether to look for a block
look_for_block = False

# Initialize a variable to store the position instruction
position_instruction = ''

def detect_colored_blocks_and_assign_position(image):
    global block_counter, look_for_block, position_instruction

    # Define the color ranges for red, blue, green, yellow
    color_ranges = {
        'red': ([0, 187, 135], [77, 255, 255]),
        'blue': ([82, 59, 75], [119, 248, 255]),
        'green': ([29, 0, 149], [119, 255, 255]),
        'yellow': ([0, 130, 201], [46, 196, 255])
    }

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for color_number, color_name in color_dict.items():
        lower, upper = color_ranges[color_name]
        # Create a mask for the current color
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Sort the contours by area in descending order and keep the largest one
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

        for contour in contours:
            # Get the bounding rectangle for the current contour
            x, y, w, h = cv2.boundingRect(contour)

            # Check if the contour is large enough (i.e., the object is at least 100 pixels)
            if cv2.contourArea(contour) < 500:
                continue

            # Check if the contour is square (i.e., a top view of a cube)
            aspect_ratio = float(w)/h
            if aspect_ratio < 0.9 or aspect_ratio > 1.1:
                continue

            # Draw the bounding rectangle on the image
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # If the flag is set, find the position for the current color block
            if look_for_block:
                positions = np.where(target_matrix == color_number)
                for pos in zip(*positions):
                    if pos not in filled_positions:
                        filled_positions.append(pos)
                        position_number = pos[0] * 4 + pos[1] + 1
                        # Put the position number on the image
                        position_instruction = f'Place at position {position_number}'
                        cv2.putText(image, position_instruction, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                        block_counter += 1
                        break
                else:
                    # If no position was found for the current color block, display 'block not needed'
                    position_instruction = 'block not needed'
                    cv2.putText(image, position_instruction, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            else:
                # If the flag is not set, display the last position instruction
                cv2.putText(image, position_instruction, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # If no contours were found, display 'no block in view'
    if not contours:
        cv2.putText(image, 'no block in view', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the block counter at the top of the image
    cv2.putText(image, f'Blocks encountered: {block_counter}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Reset the flag
    look_for_block = False

    return image

# Initialize the video capture object for the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was successfully captured
    if ret:
        # Apply the function to the current frame
        frame = detect_colored_blocks_and_assign_position(frame)

        # Display the image
        cv2.imshow('Image', frame)

    # If the spacebar is pressed, set the flag to look for a block
    if cv2.waitKey(1) & 0xFF == ord(' '):
        look_for_block = True

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# Print the last position instruction
print(position_instruction)
