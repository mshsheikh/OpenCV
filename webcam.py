import cv2
import os

# Global variables
button_clicked = False
image_counter = 0

# Callback to detect clicks
def mouse_callback(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        button_x, button_y, button_radius = 590, 440, 20
        if (x - button_x) ** 2 + (y - button_y) ** 2 <= button_radius ** 2:
            button_clicked = True

def main():
    global button_clicked, image_counter

    # Load face detection classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Access default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Unable to open camera!")
        return

    # Create output directory
    output_dir = "captured_images"
    os.makedirs(output_dir, exist_ok=True)

    # Set up mouse callback
    cv2.namedWindow('Webcam Feed')
    cv2.setMouseCallback('Webcam Feed', mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw face rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Draw capture button
        height, width = frame.shape[:2]
        button_radius = 20
        button_x = width - 50
        button_y = height - 50
        
        # White background
        cv2.circle(frame, (button_x, button_y), button_radius + 5, (255, 255, 255), -1)
        # Red button
        cv2.circle(frame, (button_x, button_y), button_radius, (0, 0, 255), -1)

        cv2.imshow('Webcam Feed', frame)

        # Save image when button clicked
        if button_clicked:
            image_path = os.path.join(output_dir, f"image_{image_counter}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image saved: {image_path}")
            image_counter += 1
            button_clicked = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
