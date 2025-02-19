from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
import speech_recognition as sr
from moviepy import VideoFileClip

# Initialize Flask App
app = Flask(__name__)

# API Key Setup
API_KEY = "your actual API key" # Replace with your actual API key
if not API_KEY:
    raise ValueError("🔑 API Key not found! Set GEMINI_API_KEY in the environment.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Root Route (Serves HTML Page)
@app.route("/")
def home():
    return render_template("index.html")

# Function to process video and transcribe audio
def process_video(video_path):
    """Extracts audio from a video and converts it to text."""
    try:
        clip = VideoFileClip(video_path)
        audio_path = "audio.wav"
        clip.audio.write_audiofile(audio_path, codec="pcm_s16le")  # Ensures compatibility

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        return model.generate_content(f"Refine this transcript:\n{text}").text.strip()
    except Exception as e:
        return f"Error processing video: {str(e)}"

# Content moderation function
def moderate_content(text):
    """Uses AI to check for inappropriate or sensitive content."""
    moderation_prompt = f"Check if the following content is appropriate for all audiences:\n{text}"
    return model.generate_content(moderation_prompt).text.strip()

# AI Content Generation Function
def generate_content(task, text):
    """AI-powered creative content generation."""
    prompt = f"Create a {task} based on the following content:\n{text}"
    return model.generate_content(prompt).text.strip()

@app.route("/transcribe", methods=["POST"])
def transcribe_video():
    """Handles video file uploads, processes transcription and moderation."""
    if "video" not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    video = request.files["video"]
    video_path = "temp.mp4"
    video.save(video_path)

    transcription = process_video(video_path)
    moderation_feedback = moderate_content(transcription)

    return jsonify({
        "transcription": transcription,
        "moderation_feedback": moderation_feedback
    })

@app.route("/generate", methods=["POST"])
def generate_ai_content():
    """Generates AI-powered content based on transcription."""
    data = request.json
    task = data.get("task")
    text = data.get("text")

    if not task or not text:
        return jsonify({"error": "Missing required parameters"}), 400

    generated_content = generate_content(task, text)
    return jsonify({"generated_content": generated_content})

if __name__ == "__main__":
    # Copy the video file to the working directory
    source_video_path = r"C:\Users\user\Downloads\Deeseek_AI Model_Video.mp4"
    destination_video_path = r"C:\Users\user\Downloads\Deeseek_AI Model_Video.mp4"
    if os.path.exists(source_video_path):
        os.system(f"copy \"{source_video_path}\" \"{destination_video_path}\"")
        app.run(debug=True)
