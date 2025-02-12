# Real-Time Face Detection and Image Capture

This Python application uses OpenCV and PyQt5 to access your computer's webcam, detect faces in real-time, and capture images using a clickable button. The application features an interactive GUI where the cursor changes to indicate when it’s hovering over the capture button. Captured images are saved to a local directory.

## Features
- **Real-Time Face Detection**: Detects human faces in the webcam feed using Haar Cascade classifiers.
- **Image Capture via GUI**: Provides a clickable button within a PyQt5 interface for capturing images.
- **Dynamic Cursor Change**: Automatically changes the OS cursor to a pointing hand when hovering over the capture button.
- **Image Saving**: Captured images are saved to a directory named `captured_images`.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- PyQt5

## Installation

1. Install the required dependencies:
   ```bash
   pip install opencv-python PyQt5
   ```

## Running the Application

1. Launch the application by running:
   ```bash
   python webcam.py
   ```
2. A window will appear displaying the live webcam feed with a clickable button in the bottom-right corner.
3. **Face Detection**: Faces detected in the feed are highlighted with green rectangles.
4. **Cursor Interaction**: When you move your mouse over the capture button, the cursor will change to a pointing hand, indicating that the button is clickable.
5. **Image Capture**: Click the button to capture an image. The captured image will be saved in the `captured_images` directory.
6. Close the window to exit the application.

## Directory Structure
```
OpenCV/
├── captured_images/
├── webcam.py
├── README.md
```

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

Enjoy using the Real-Time Face Detection and Image Capture application! If you have any questions or feedback, please feel free to reach out.
