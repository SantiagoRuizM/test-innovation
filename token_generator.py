import os
import datetime

def token_generator():

    secret_passwrod = "Test-innovation1"

    payload = {
    'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10)  
    }

    token = jwt.encode(payload, secret_passwrod, algorithm="HS256")

    return token