import os
import twilio
from twilio.rest import Client

twilioAccSSID = 'ACf5da1645597d0798f4ff3be7c16dfeb4'
twilioAccTOKEN = 'd0be0aae9bb8c7ba9a016075df62fcd6'

client = Client(twilioAccSSID,twilioAccTOKEN)

client.messages.create(
        body = "I love you Keen she is my baby girl",
        to = "+6588159408",
        from_ = "16314961976"
    )


