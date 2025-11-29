import google.generativeai as genai
import os
import json
from dotenv import load_dotenv  # <--- NEW IMPORT
from prompt import VISION_PROMPT, ARTIST_PROMPT, ENGINEER_PROMPT, QA_PROMPT

# 1. Load environment variables from .env file
load_dotenv()

# 2. Retrieve the key safely
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ API Key not found! Make sure you have a .env file with GOOGLE_API_KEY defined.")

# 3. Configure Gemini
genai.configure(api_key=api_key)

# Use Flash for speed
model = genai.GenerativeModel('gemini-pro-latest')

# ... (The rest of the functions remain the same) ...

def clean_response(text):
    return text.replace('```json', '').replace('```python', '').replace('```', '').strip()

def agent_vision(user_input):
    print(f"👁️  Vision Agent: Analyzing '{user_input}'...")
    response = model.generate_content(VISION_PROMPT.format(user_input=user_input))
    return clean_response(response.text)

def agent_artist(design_json):
    print("🎨 Artist Agent: Painting procedural assets...")
    response = model.generate_content(ARTIST_PROMPT.format(design_json=design_json))
    return clean_response(response.text)

def agent_engineer(design_json, artist_code):
    print("⚙️  Engineer Agent: Assembling game engine...")
    response = model.generate_content(ENGINEER_PROMPT.format(design_json=design_json, artist_code=artist_code))
    return clean_response(response.text)

def agent_qa(raw_code):
    print("🐞 QA Agent: Playtesting and fixing bugs...")
    response = model.generate_content(QA_PROMPT.format(code=raw_code))
    return clean_response(response.text)