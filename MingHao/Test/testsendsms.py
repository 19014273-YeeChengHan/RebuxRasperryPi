import os
import twilio
from twilio.rest import Client

twilioAccSSID = 'ACf5da1645597d0798f4ff3be7c16dfeb4'
twilioAccTOKEN = '5bfb72d945db84a6cf489d8f648e8c82'

client = Client(twilioAccSSID,twilioAccTOKEN)

client.messages.create(
        body = "I love you Keen she is my baby girl",
        to = "+6588159408",
        from_ = "16314961976"
    )


