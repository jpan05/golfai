from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import shutil
import os
from pose_estimation import PoseEstimator
from video_processing import VideoProcessor
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads" 
OUTPUT_DIR = "processed_videos"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app.mount("/processed_videos", StaticFiles(directory="processed_videos"), name="processed_videos")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Handles file upload and runs pose estimation."""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the video
    processed_video_path = process_video(file_path)

    return {"message": "File processed", "processed_video": processed_video_path}


def process_video(video_path):
    """Runs pose estimation on the uploaded video and saves the output."""
    processor = VideoProcessor(video_path)
    estimator = PoseEstimator()
    
    frames = processor.get_frames()

    output_path = os.path.join(OUTPUT_DIR, "processed_" + os.path.basename(video_path))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    frame_height, frame_width = frames[0].shape[:2]
    out = cv2.VideoWriter(output_path, fourcc, 30, (frame_width, frame_height))

    for frame in frames:
        results = estimator.process_frame(frame)
        frame_with_landmarks = estimator.draw_landmarks(frame, results)
        out.write(frame_with_landmarks)

    out.release()
    return output_path

# checks the name of the file so it can only be run in main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
