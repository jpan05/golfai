import cv2
import mediapipe as mp

class PoseEstimator:
    def __init__(self, model_complexity=2, min_detection_conf=0.7, min_tracking_conf=0.7):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(model_complexity=model_complexity, 
                                      min_detection_confidence=min_detection_conf,
                                      min_tracking_confidence=min_tracking_conf,
                                      smooth_landmarks=True)
        self.mp_drawing = mp.solutions.drawing_utils

    def process_frame(self, frame):
        """Processes a single frame and returns pose landmarks."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb_frame)

    def draw_landmarks(self, frame, results):
        """Draws pose landmarks on the frame."""
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return frame
