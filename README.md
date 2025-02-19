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
### │-- static/                 # Static files (CSS, JS, Images)
### │-- templates/              # HTML Templates
### │   ├── index.html          # Main UI Page
### │-- app.py                  # Main Flask Application
### │-- requirements.txt        # Dependencies List
### │-- README.md               # Project Documentation

# Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Set Up API Key

 Replace API_KEY in app.py with your actual Google Gemini API key.
 API_KEY = "your_actual_api_key"

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









# Project Title: AI-Powered Content Generation & Moderation System

### Introduction

This project involves building an AI-powered content generation and moderation system using Google Gemini AI. The system will perform text summarization and classify user-generated content based on appropriateness. It includes functionalities such as content moderation, toxicity detection, and spam analysis.

# 1. Project Setup

### 1.1 Prerequisites

Python 3.7+

Google Generative AI SDK (google.generativeai)

getpass for secure API key entry

# 1.2 Installation
pip install google-generativeai

# 1.3 API Configuration

The API key is securely entered and used to authenticate with Google Gemini AI:
import getpass
import google.generativeai as genai

api_key = getpass.getpass("Enter your Gemini API key: ")
genai.configure(api_key=api_key)

# AI-Powered Content Generation

### Text Summarization

Objective: Summarize a given text efficiently.

Implementation:

A prompt is created instructing the model to summarize the given text.

The AI generates a concise summary.
def summarize_text(text):
    """
    Summarizes the input text using Google Gemini AI.
    """
    prompt = f"Summarize the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

 input_models:--
 Google Gemini AI is a cutting-edge, multimodal artificial intelligence model...

 # Content Moderation System Development

### Content Classification

Objective: Classify user-generated content based on appropriateness.

Classification Categories:

Allow (0-25%): Low or no inappropriate content.

Flag for Review (25%-60%): Moderate inappropriate content.

Block (>60%): High inappropriate content.

## Code:-
def moderate_content(text):
    """
    Classifies user-generated content based on appropriateness.
    """
    prompt = f"""Analyze the content and classify it as:
    - Allow (0-25% inappropriate content)
    - Flag for Review (25%-60%)
    - Block (>60%)\n\nContent: "{text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Toxicity Scoring

Objective: Assign a toxicity score (0-100) based on the level of inappropriate content.

## Code:
def content_scoring(text):
    """
    Assigns a toxicity score (0-100) based on inappropriate content levels.
    """
    prompt = f"""Assign a toxicity score (0-100) for the following content:\n\n"{text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Toxicity & Spam Detection

Objective: Analyze text for toxicity level, spam probability, and provide a recommendation.

## Code:-
def detect_toxicity(text):
    """
    Detects toxicity and spam levels in text.
    """
    prompt = f"""Analyze the content for:
    - Toxicity Level (Low, Medium, High)
    - Spam Probability (Low, Medium, High)
    - Recommendation (Allow, Review, Block)\n\nContent: "{text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

 ## Example Test Cases:-
 test_contents = [
    "This is a friendly and safe post about AI technology.",
    "Some people use hate speech and offensive language online.",
    "This message contains inappropriate and explicit content."
]

for i, content in enumerate(test_contents, 1):
    print(f"\nModeration Result {i}:\n", moderate_content(content))
    print(f"\nContent Score {i}:\n", content_scoring(content))
    print(f"\nToxicity Analysis {i}:\n", detect_toxicity(content))


# Test Cases & Results

Provide 3-5 test cases covering:

AI-generated text summarization.

Content moderation classification.

Toxicity and spam detection outputs.

# Summary

Implemented Text Summarization using Gemini AI.

Developed a Content Moderation System with:

Classification (Allow, Flag for Review, Block)

Toxicity Scoring (0-100 scale)

Toxicity & Spam Analysis

Code structured professionally for clarity and scalability.
Outcome: A robust AI-driven system that generates and moderates content efficiently, ensuring safe and appropriate user interactions.

