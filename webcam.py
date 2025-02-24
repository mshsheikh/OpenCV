import sys
import cv2
import os
from PyQt5 import QtWidgets, QtGui, QtCore

class VideoWidget(QtWidgets.QLabel):
    def __init__(self, capture, parent=None):
        super().__init__(parent)
        self.capture = capture
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrame)
        self.timer.start(30)  # 30 FPS
        self.mouse_x, self.mouse_y = 0, 0
        self.button_radius = 20  # Button Radius
        self.button_x = 0
        self.button_y = 0
        self.image_counter = 0
        self.output_dir = "captured_images"
        os.makedirs(self.output_dir, exist_ok=True)

    def nextFrame(self):
        ret, frame = self.capture.read()
        if not ret:
            return
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        self.button_x = width - 50
        self.button_y = height - 50

        # Draw button
        cv2.circle(frame, (self.button_x, self.button_y), self.button_radius + 5, (255, 255, 255), -1)
        # Using widget coordinates (if your QLabel size differs from the frame, adjust for scaling)
        dist_sq = (self.mouse_x - self.button_x) ** 2 + (self.mouse_y - self.button_y) ** 2
        is_hovering = dist_sq <= self.button_radius**2
        button_color = (0, 255, 0) if is_hovering else (0, 0, 255)
        cv2.circle(frame, (self.button_x, self.button_y), self.button_radius, button_color, -1)
        if is_hovering:
            cv2.putText(frame, "CLICK", (self.button_x - 30, self.button_y - 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Convert frame to QImage and display
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.setPixmap(QtGui.QPixmap.fromImage(qt_image))

    def mouseMoveEvent(self, event):
        self.mouse_x = event.x()
        self.mouse_y = event.y()
        # Change cursor when hovering over the button
        dist_sq = (self.mouse_x - self.button_x) ** 2 + (self.mouse_y - self.button_y) ** 2
        if dist_sq <= self.button_radius**2:
            self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def mousePressEvent(self, event):
        # Capture the image on click
        if event.button() == QtCore.Qt.LeftButton:
            dist_sq = (self.mouse_x - self.button_x) ** 2 + (self.mouse_y - self.button_y) ** 2
            if dist_sq <= self.button_radius**2:
                # Save the image
                ret, frame = self.capture.read()
                if ret:
                    frame = cv2.flip(frame, 1)
                    image_path = os.path.join(self.output_dir, f"image_{self.image_counter}.jpg")
                    cv2.imwrite(image_path, frame)
                    print(f"Image saved: {image_path}")
                    self.image_counter += 1

def main():
    app = QtWidgets.QApplication(sys.argv)
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print("Unable to open camera!")
        return
    video_widget = VideoWidget(capture)
    video_widget.setMouseTracking(True)  # Mouse tracking
    video_widget.resize(640, 480)
    video_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
