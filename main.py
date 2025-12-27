from fastapi import FastAPI, Response
from pydantic import BaseModel
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
BASE_URL = os.getenv("BASE_URL")

# Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app = FastAPI(title="Simple Twilio Call System")

# Request model
class CallRequest(BaseModel):
    phone_number: str


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/call")
def call_number(data: CallRequest):
    """
    Triggers an outbound phone call
    """
    call = twilio_client.calls.create(
        to=data.phone_number,
        from_=TWILIO_PHONE_NUMBER,
        url=f"{BASE_URL}/twilio/webhook"
    )

    return {
        "success": True,
        "call_sid": call.sid
    }


# @app.post("/twilio/webhook")
# def twilio_webhook():
#     """
#     Twilio hits this endpoint when the call is answered
#     """
#     response = VoiceResponse()
#     response.say(
#         "Hello. This is an automated call from our system. Thank you.",
#         voice="alice"
#     )

#     return Response(
#         content=str(response),
#         media_type="application/xml"
#     )


@app.api_route("/twilio/webhook", methods=["GET", "POST"])
def twilio_webhook():
    print("Twilio webhook hit")
    response = VoiceResponse()
    response.say(
        "Hello. This is an automated call from our system. Thank you.",
        voice="alice"
    )

    return Response(
        content=str(response),
        media_type="application/xml"
    )
