import cv2

class VideoProcessor:
    def __init__(self, video_path, resize_factor=0.7):
        self.video_path = video_path
        self.resize_factor = resize_factor

    def get_frames(self):
        """Reads video frames and returns a list of resized frames."""
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError(f"Error: Could not open video at {self.video_path}")

        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Resize the frame
            frame_resized = cv2.resize(frame, (0, 0), fx=self.resize_factor, fy=self.resize_factor)
            frames.append(frame_resized)

        cap.release()
        return frames
