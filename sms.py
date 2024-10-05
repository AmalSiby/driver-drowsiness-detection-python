import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the account SID and Auth Token from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='The Driver is feeling Drowsy, Check on him',
    from_='+91 9092704120',
    to='+91 8610405995'
)

print(message.sid)
