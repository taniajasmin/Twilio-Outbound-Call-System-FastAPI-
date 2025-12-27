# Twilio Outbound Call System (FastAPI)

A minimal FastAPI-based outbound calling system using Twilio.  
This project demonstrates how to programmatically place phone calls and play a spoken message using Twilio’s built-in Text-to-Speech (TwiML).

---

## Features

- Outbound calls to any valid phone number  
- Built-in Twilio Text-to-Speech (no audio files)  
- Simple webhook-based call flow  
- Single-file backend, easy to extend  

---

## Tech Stack

- Python
- FastAPI
- Twilio Voice API
- Uvicorn
- ngrok

---

## Project Structure
```yaml
twilio-call/
├── main.py
├── .env
└── requirements.txt
```

---

## Setup

1. Install dependencies:
```txt
pip install -r requirements.txt
```
2. Create `.env`:
```txt
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
BASE_URL=[https://xxxx.ngrok-free.dev](https://pluckiest-trimorphous-ivana.ngrok-free.dev
)
```
3. Run server:
```txt
uvicorn main:app --reload
```

4. Expose with ngrok (run this):
```txt
ngrok http 8000
```

---

## API

### Start a Call
```
POST /call
{
"phone_number": "+8801XXXXXXXXX"
}
```

### Twilio Webhook
```
GET | POST /twilio/webhook
```
Returns TwiML that speaks a message during the call.

---

## Notes

- `TWILIO_PHONE_NUMBER` must be a Twilio-owned or verified number  
- `BASE_URL` must be publicly accessible (HTTPS)  
- If the webhook is unreachable, the call will end immediately  

---
