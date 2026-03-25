🤖 Voice Bot — AI-Powered Voice Assistant with FastAPI & Twilio
A Python-based voice bot that handles automated phone interactions using FastAPI, Twilio, and external AI integrations. Designed as a foundation for replacing or augmenting traditional receptionist workflows through intelligent voice automation.

✨ Features

Automated inbound/outbound voice call handling via Twilio
RESTful webhook endpoints built with FastAPI
Integration with external AI/NLP services via Requests
Environment-based configuration using python-dotenv
Async-ready server with Uvicorn


🏗️ Project Structure
Voice_bot/
├── app/               # Core application logic and route handlers
├── .gitignore         # Environment files and secrets excluded
├── requirements.txt   # Python dependencies
└── README.md

🛠️ Tech Stack
TechnologyPurposePythonCore languageFastAPIREST API framework for webhook endpointsUvicornASGI server for async request handlingTwilioVoice call management and telephony integrationRequestsExternal API communicationpython-dotenvSecure environment variable management

🚀 Getting Started
Prerequisites

Python 3.9+
A Twilio account with a phone number
A .env file with your credentials (see below)

Installation

Clone the repository

bash   git clone https://github.com/cactusjhack/Voice_bot.git
   cd Voice_bot

Create and activate a virtual environment

bash   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bash   pip install -r requirements.txt

Set up environment variables — create a .env file:

env   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_number

Run the server

bash   uvicorn app.main:app --reload

🔧 How It Works

Twilio routes incoming calls to the FastAPI webhook endpoints
The bot processes the voice input and determines the appropriate response
External AI/API calls are made via Requests to generate intelligent replies
The response is converted back to voice and delivered through Twilio


🎯 Use Case
This project was built to explore the automation of reception and customer service workflows using voice AI — reducing manual intervention in routine call handling while maintaining a natural conversational experience.

👤 Author
Jhackson Palacios Perea
Software Development Student — ITM, Medellín, Colombia
github.com/cactusjhack
