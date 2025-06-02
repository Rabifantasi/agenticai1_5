from litellm import completion
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

def use_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        api_key=gemini_key,
        messages=[{ "content": "Hello, how are you?", "role": "user" }]
    )
    print(response.choices[0].message.content.strip())

use_gemini()
