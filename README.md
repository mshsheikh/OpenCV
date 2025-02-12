# Real-Time Face Detection and Image Capture

This Python application uses OpenCV to access your computer's webcam, detect faces in real-time, and capture images with a clickable button. The captured images are saved to a local directory.

## Features
- **Real-Time Face Detection**: Detects human faces in the webcam feed using Haar Cascade classifiers.
- **Image Capture**: Allows you to capture images by clicking a button on the screen.
- **User-Friendly Interface**: Displays a red button for capturing images and green bounding boxes around detected faces.
- **Image Saving**: Saves captured images to a directory named `captured_images`.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- A working webcam

1. Install the required dependencies:
   ```bash
   pip install opencv-python
   ```

2. Run the application:
   ```bash
   python webcam.py
   ```

## Usage
1. Launch the application by running `webcam.py`.
2. A window titled "Webcam Feed" will open, displaying the live webcam feed.
3. Faces detected in the feed will be highlighted with green rectangles.
4. To capture an image:
   - Click the red button in the bottom-right corner of the window.
   - The captured image will be saved in the `captured_images` directory.
5. Press the `q` key to exit the application.

## Directory Structure
```
OpenCV/
├── captured_images/
├── webcam.py
├── README.md
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

Enjoy using the Real-Time Face Detection and Image Capture application! If you have any questions, feel free to reach out.
