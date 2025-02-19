import os
import getpass
import google.generativeai as genai

api_key = getpass.getpass("Enter your Gemini API key: ")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_text(text):
    """
    Summarizes the input text using Google Gemini AI.
    """
    prompt = f"Summarize the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()


input_text = """Google Gemini AI is a cutting-edge, multimodal artificial intelligence model developed to handle diverse data formats, including text, images, audio, and video.
Designed for efficiency and scalability, Gemini AI provides a range of advanced capabilities such as natural language processing, content generation, summarization, and contextual understanding.
The model is built to enhance AI-driven applications across industries, supporting tasks like automated customer support, real-time translation, and intelligent content recommendations.
With state-of-the-art machine learning techniques, Gemini AI optimizes computational resources while maintaining high performance, making it a valuable tool for enterprises and developers looking to integrate AI into their workflows."""

summary = summarize_text(input_text)
print("Summary:\n", summary)


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

def content_scoring(text):
    """
    Assigns a toxicity score (0-100) based on inappropriate content levels.
    """
    prompt = f"""Assign a toxicity score (0-100) for the following content:\n\n"{text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

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

test_contents = [
    "This is a friendly and safe post about AI technology.",
    "Some people use hate speech and offensive language online.",
    "This message contains inappropriate and explicit content."
]

for i, content in enumerate(test_contents, 1):
    print(f"\nModeration Result {i}:\n", moderate_content(content))
    print(f"\nContent Score {i}:\n", content_scoring(content))
    print(f"\nToxicity Analysis {i}:\n", detect_toxicity(content))
