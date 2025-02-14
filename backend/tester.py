import cv2
import mediapipe as mp

#initialize mediapipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=2, 
                    min_detection_confidence=0.7, 
                    min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# initialize opencv
cap = cv2.VideoCapture('D:/golfai/videos/testvideo1.mp4')

# Check if the video was successfully opened
if not cap.isOpened():
   print("Error: Could not open video.")
   exit()

resize_factor = 0.7  

while True:
    ret, frame = cap.read()

    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get the pose landmarks
    results = pose.process(rgb_frame)

    # If landmarks are found, draw them on the image
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    frame_resized = cv2.resize(frame, (0, 0), fx=resize_factor, fy=resize_factor)

    # display result
    cv2.imshow("Pose Tracking", frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()