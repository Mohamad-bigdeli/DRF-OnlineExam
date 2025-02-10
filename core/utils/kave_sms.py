from kavenegar import *

class SmsMessage():

    def __init__(self, receptor, message):
        self.receptor = receptor
        self.message = message

    def send_sms(self):
        try:
            api = KavenegarAPI('4459652B307562487462724D2F52664E786F493976434E4A784334336D30494F794834645939484C50704D3D')
            params = {
                'sender': '',#optional
                'receptor': self.receptor,#multiple mobile number, split by comma
                'message': self.message,
            } 
            response = api.send_sms(params)
            print(response)
        except APIException as e: 
            print(e)
        except HTTPException as e: 
            print(e)