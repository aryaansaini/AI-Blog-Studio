import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_blog(topic):
    prompt = f"""
    Write a professional blog on the topic: {topic}

    Include:
    - Title
    - Introduction
    - Main Content
    - Conclusion
    """

    response = model.generate_content(prompt)
    return response.text