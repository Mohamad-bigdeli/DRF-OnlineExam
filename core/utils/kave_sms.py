#!/usr/bin/env python
from kavenegar import *

def send_sms(receptor, message):
    try:
        api = KavenegarAPI("4459652B307562487462724D2F52664E786F493976434E4A784334336D30494F794834645939484C50704D3D")
        params = {
            'sender': '',#optional
            'receptor': receptor,#multiple mobile number, split by comma
            'message': message,
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)