import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture('D:/golfai/videos/testvideo1.mp4')

# Check if the video was successfully opened
if not cap.isOpened():
   print("Error: Could not open video.")
   exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get the pose landmarks
    results = pose.process(rgb_frame)

    # If landmarks are found, draw them on the image
    if results.pose_landmarks:
        # Draw landmarks (skeleton)
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Display the resulting frame with pose landmarks
    cv2.imshow("Pose Tracking", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
