#app/main.py

from fastapi import FastAPI
from fastapi.responses import Response # <- importar esta

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "voice -bot está corriendo"}

@app.post("/voice")
def voice_response():
    xml_response = """
    <Response>
        <Say voice="alice" language="es-MX">
        <![CDATA[ 
            Hola, le llamamos de la EPS para recordarle su cita medica mañana a las 10 de la mañana.
            si desea confirmar, por favor presione 1.
            ]]> 
        </Say>
    </Response>
    """
    return Response(content=xml_response, media_type="application/xml")

from app.twilio_handler import make_call

@app.get("/call")
def test_call():
    phone = input("Numero a llamar (con +573127550777): ")
    webhook = "https://5c5b-2800-e2-2980-52f-2d26-82c-262e-c6a3.ngrok-free.app/voice"
    print(f"Llamando a {phone} usando webhook: {webhook}")

    sid = make_call(phone, webhook)
    print(f"Llamada iniciada. SID: {sid}")
    return {"message": "Llamada iniciada", "sid": sid}

from app.tts import text_to_speech_es
import os 

@app.get("/generate-audio")
def generate_audio():
    text = "Hola, le llamamos de su EPS para recordarle que tiene cita medica mañana a las 10 de la mañana. si desea confirmar, por favor diga si."
    audio_path = text_to_speech_es(text, "audio/cita.mp3")
    return {"message": "Audio generado", "path": audio_path}