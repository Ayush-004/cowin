# test_otp.py

from otp_generator import OTPGenerator
from otp_verifier import OTPVerifier

# Generate OTP
generator = OTPGenerator()
otp = generator.generate_otp()
print("Generated OTP:", otp)

# Verify OTP
user_input = input("Enter OTP for verification: ")
verifier = OTPVerifier(otp)
if verifier.verify(user_input):
    print("OTP verification successful!")
else:
    print("OTP verification failed!")
