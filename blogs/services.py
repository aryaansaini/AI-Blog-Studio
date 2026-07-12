from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_blog(topic):
    prompt = f"""
Write a professional blog on the topic: "{topic}".

Requirements:
- Add a professional title as the first line using Markdown (# Title)
- Include Introduction
- Main Content
- Advantages
- Challenges
- Future Scope
- Conclusion

Return only the blog in Markdown.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 4096,
        }
    )

    return response.text