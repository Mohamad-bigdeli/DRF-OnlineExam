import threading
from django.core.cache import cache

class ThreadSms(threading.Thread):
    def __init__(self, sms_message):
        threading.Thread.__init__(self)
        self.sms_message = sms_message
    
    def run(self):
        self.sms_message.send_sms()