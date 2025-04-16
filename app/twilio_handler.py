#app/twilio_handley.py

import os 
from dotenv import load_dotenv
from twilio.rest import Client

# Carga las variables del archivo .env
load_dotenv()

# Autenticacion con twilio
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

Client = Client(account_sid, auth_token)

def make_call(to_number: str, webhook_url: str):
    """
    Inicie una llamada usando Twilio al numero especificado, 
    y Twilio usara webhook_url para saber que decir.
    
    """
    
    call = Client.calls.create(
    to=to_number,
    from_=twilio_number,
    url=webhook_url
    )
    return call.sid 