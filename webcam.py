import cv2
import os

# Global variables
button_clicked = False
image_counter = 0

# Callback to detect clicks
def mouse_callback(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:  # Check for left mouse button click
        # Define the button's position and radius
        button_x, button_y, button_radius = 590, 440, 20  # Center and radius of the circle
        # Check if the click is inside the circle using distance formula
        if (x - button_x) ** 2 + (y - button_y) ** 2 <= button_radius ** 2:
            button_clicked = True

def main():
    global button_clicked, image_counter

    # Access default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Webcam check
    if not cap.isOpened():
        print("Unable to open camera!")
        return

    # Create a directory to save captured images
    output_dir = "captured_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set up mouse callback for detecting button clicks
    cv2.namedWindow('Webcam Feed')
    cv2.setMouseCallback('Webcam Feed', mouse_callback)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Frame read
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Frame dimensions
        height, width = frame.shape[:2]

        # Button properties
        button_radius = 20  # Smaller button size
        button_x = width - 50  # Position in the bottom-right corner
        button_y = height - 50

        # White border
        cv2.circle(frame, (button_x, button_y), button_radius + 5, (255, 255, 255), -1)  # White filled circle

        # Red button
        cv2.circle(frame, (button_x, button_y), button_radius, (0, 0, 255), -1)  # Red filled circle

        # Display
        cv2.imshow('Webcam Feed', frame)

        # Click will save as an image
        if button_clicked:
            image_path = os.path.join(output_dir, f"image_{image_counter}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image saved: {image_path}")
            image_counter += 1
            button_clicked = False  # Reset the button

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
