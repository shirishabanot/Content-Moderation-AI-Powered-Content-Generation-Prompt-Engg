# pip install---flask
# pip install---google.generativeai
# pip install---speech_recognition
# pip install---moviepy

# API_KEY = "your actual API key"

# GenerativeModel.(gemini-1.5-flash)

from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
import speech_recognition as sr
from moviepy import VideoFileClip

# Initialize Flask App
app = Flask(__name__)

# API Key Setup
API_KEY = os.getenv("GEMINI_API_KEY")  # Store API Key as an environment variable
if not API_KEY:
    raise ValueError("🔑 API Key not found! Set GEMINI_API_KEY in the environment.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Root Route (HTML Page for Uploading Video)
@app.route("/")
def home():
    return render_template("index.html")

# Function to process video and transcribe audio
def process_video(video_path):
    """Extracts audio from a video and converts it to text."""
    try:
        audio_path = "temp_audio.wav"

        # Extract audio from the video
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path, codec="pcm_s16le")

        # Transcribe audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        return text.strip()
    except Exception as e:
        return f"Error processing video: {str(e)}"

# AI Content Moderation Function
def moderate_content(text):
    """Uses AI to check for inappropriate or sensitive content."""
    moderation_prompt = f"Check if the following content is appropriate for all audiences:\n{text}"
    return model.generate_content(moderation_prompt).text.strip()

# ✅ API Endpoint: Transcribe Video
@app.route("/transcribe", methods=["POST"])
def transcribe_video():
    """Handles video file uploads, processes transcription and moderation."""
    if "video" not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    video = request.files["video"]
    
    # Save uploaded video
    video_path = os.path.join("uploads", video.filename)
    os.makedirs("uploads", exist_ok=True)
    video.save(video_path)

    # Process Video
    transcription = process_video(video_path)
    moderation_feedback = moderate_content(transcription)

    return jsonify({
        "transcription": transcription,
        "moderation_feedback": moderation_feedback
    })

if __name__ == "__main__":
    app.run(debug=True)
