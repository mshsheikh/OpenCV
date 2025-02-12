import cv2

def main():
    # Access default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Webcam check
    if not cap.isOpened():
        print("Unable to open camera!")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Frame read
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        # Frame flip (1 means horizontal flip)
        frame = cv2.flip(frame, 1)

        # Display
        cv2.imshow('Webcam Feed', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()