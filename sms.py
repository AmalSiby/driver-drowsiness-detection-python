# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ[ACbcfeeb7c16124200b5f68dbea839397e]
auth_token = os.environ[92e12713a342cdb17c7a5602bf3fbfee]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='The Driver is felling Drowsy, Check on him',
         from_='+91 9092704120',
         to='+91 8610405995'
     )

print(message.sid)
