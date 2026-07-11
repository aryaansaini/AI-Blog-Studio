from google import genai
from decouple import config

client = genai.Client(api_key=config("GEMINI_API_KEY"))

models = [
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-2.0-flash",
    "gemini-2.5-flash",
]

for m in models:
    try:
        print(f"Testing: {m}")
        response = client.models.generate_content(
            model=m,
            contents="Say Hello"
        )
        print("SUCCESS:", m)
        print(response.text)
        break
    except Exception as e:
        print("FAILED:", m)
        print(e)