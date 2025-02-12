import cv2
import os

# Global variables
button_clicked = False
image_counter = 0
mouse_x, mouse_y = 0, 0  # Track mouse position

# Callback track movement
def mouse_callback(event, x, y, flags, param):
    global button_clicked, mouse_x, mouse_y
    mouse_x, mouse_y = x, y  # Update mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        button_x, button_y, button_radius = 590, 440, 20
        if (x - button_x) ** 2 + (y - button_y) ** 2 <= button_radius ** 2:
            button_clicked = True

def main():
    global button_clicked, image_counter, mouse_x, mouse_y

    # Face detection classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open camera!")
        return

    output_dir = "captured_images"
    os.makedirs(output_dir, exist_ok=True)

    cv2.namedWindow('Webcam Feed')
    cv2.setMouseCallback('Webcam Feed', mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        frame = cv2.flip(frame, 1)

        # Face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Button properties
        height, width = frame.shape[:2]
        button_radius = 20
        button_x = width - 50
        button_y = height - 50

        # Hover detection
        distance_sq = (mouse_x - button_x)**2 + (mouse_y - button_y)**2
        is_hovering = distance_sq <= button_radius**2

        # Interactive button
        cv2.circle(frame, (button_x, button_y), button_radius + 5, (255, 255, 255), -1)
        button_color = (0, 255, 0) if is_hovering else (0, 0, 255)  # Green when hovering
        cv2.circle(frame, (button_x, button_y), button_radius, button_color, -1)

        # Pointer
        if is_hovering:
            cv2.putText(frame, "CLICK", (button_x - 30, button_y - 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow('Webcam Feed', frame)

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
