from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_blog(topic):
    prompt = f"""
    Write a professional blog on the topic: {topic}

    Include:
    - Title
    - Introduction
    - Main Content
    - Conclusion
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text