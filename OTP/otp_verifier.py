# otp_verifier.py

class OTPVerifier:
    def __init__(self, otp):
        self.otp = otp

    def verify(self, user_input):
        return user_input == self.otp
