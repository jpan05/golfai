import { useState } from "react";
import axios from "axios";

export default function Upload() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [videoPreview, setVideoPreview] = useState<string | null>(null);
  const [processedVideo, setProcessedVideo] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setVideoPreview(URL.createObjectURL(file));
      setProcessedVideo(null);
      setError(null);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a video file first');
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:8000/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setProcessedVideo(`http://localhost:8000/${response.data.processed_video}`);
    } catch (err) {
      setError('Failed to upload and process video. Please try again.');
      console.error('Upload error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Golf Swing Analysis</h1>
      
      <div>
        <input
          type="file"
          accept="video/*"
          onChange={handleFileSelect}
          id="video-upload"
        />
      </div>

      {selectedFile && (
        <p>Selected: {selectedFile.name}</p>
      )}

      {videoPreview && (
        <div>
          <h3>Original Video</h3>
          <video src={videoPreview} controls width="500" />
          <div>
            <button onClick={handleUpload} disabled={loading}>
              {loading ? 'Processing...' : 'Analyze Swing'}
            </button>
          </div>
        </div>
      )}

      {processedVideo && (
        <div>
          <h3>Processed Video</h3>
          <video src={processedVideo} controls width="500" />
        </div>
      )}

      {error && (
        <p>{error}</p>
      )}
    </div>
  );
}