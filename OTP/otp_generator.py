# otp_generator.py

import random

class OTPGenerator:
    def __init__(self, length=6):
        self.length = length

    def generate_otp(self):
        otp = ""
        for _ in range(self.length):
            otp += str(random.randint(0, 9))
        return otp
