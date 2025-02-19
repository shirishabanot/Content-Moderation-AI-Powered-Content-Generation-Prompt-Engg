# Content-Moderation-AI-Powered-Content-Generation-Prompt-Engg
## 📌 Project Overview

This project is a Flask-based AI-powered system that processes video files to:

Extract audio and transcribe speech to text.

Moderate content for inappropriate or sensitive material.

Generate AI-powered content such as podcast scripts, summaries, and presentation scripts.

## 🚀 Features

Video Transcription: Extracts audio from an uploaded video and converts it into text.

Content Moderation: Uses AI to analyze the transcription and check for inappropriate content.

AI Content Generation: Generates creative content (e.g., summaries, podcast scripts) based on the transcribed text.

Web Interface: Provides a user-friendly HTML UI for uploading videos and generating AI-driven content.

## 🏗️ Tech Stack

Backend: Flask

Frontend: HTML, CSS, JavaScript (jQuery)

AI Models: Google Gemini API for content moderation and AI text generation

Libraries:

google.generativeai (for AI-powered content generation and moderation)

speech_recognition (for speech-to-text conversion)

moviepy (for audio extraction from video)


# 📂 Project Structure

# /ai_video_transcription
## │-- static/                 # Static files (CSS, JS, Images)
## │-- templates/              # HTML Templates
## │   ├── index.html          # Main UI Page
## │-- app.py                  # Main Flask Application
## │-- requirements.txt        # Dependencies List
## │-- README.md               # Project Documentation

# Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

## Set Up API Key

## Replace API_KEY in app.py with your actual Google Gemini API key.
## API_KEY = "your_actual_api_key"

## Run the Flask Application
python app.py

# Access the Web Interface

Open a web browser and navigate to:
## http://127.0.0.1:5000/

# 📌 How It Works

1️⃣ Upload a Video: Select an MP4 file from your system and upload it.
2️⃣ Transcription Process: The backend extracts audio, converts it to text, and displays the transcript.
3️⃣ Content Moderation: AI checks for inappropriate content and provides feedback.
4️⃣ Generate AI Content: Users can select a task (e.g., Podcast Script, Summary) and generate AI-powered content.

# 📝 Version Control & Best Practices

Meaningful Commits: Ensure each commit message is clear (e.g., Added video processing logic).

Branching: Follow a structured branching strategy (e.g., feature/content-generation).

README & Documentation: Maintain proper documentation for easier collaboration.
