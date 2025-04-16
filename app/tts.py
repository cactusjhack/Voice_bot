#app/tts.py

import os 
import requests
from dotenv import load_dotenv 

load_dotenv() 

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "21m00Tcm4TlvDq8ikwAM" # puedes cambiar esta ID por una voz español 

def text_to_speech_es(text: str, output_path: str = "audio/output/.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-type": "application/json"
    }

    data = {
        "text": text,
        "voice_setting": {
            "stability": 0.5,
            "similatary_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f"Error generando voz: {response.text}")