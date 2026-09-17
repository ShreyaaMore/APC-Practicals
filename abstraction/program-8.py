# 8.	Create an abstract class Authentication with an abstract method authenticate(). Implement the method using:
# a)	Password authentication 
# b)	OTP authentication 
# c)	Biometric authentication 
# Demonstrate abstraction by interacting with objects through the abstract interface.

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, stored_username, stored_password):
        self.stored_username = stored_username
        self.stored_password = stored_password

    def authenticate(self, credentials):
        user, pwd = credentials.get("username"), credentials.get("password")
        if user == self.stored_username and pwd == self.stored_password:
            return True, "Password verified successfully."
        return False, "Invalid username or password."


class OTPAuthentication(Authentication):
    def __init__(self, registered_mobile, active_otp):
        self.registered_mobile = registered_mobile
        self.active_otp = str(active_otp)

    def authenticate(self, credentials):
        mobile, otp = credentials.get("mobile"), str(credentials.get("otp"))
        if mobile == self.registered_mobile and otp == self.active_otp:
            return True, "One-Time Password verified successfully."
        return False, "Incorrect or expired OTP."


class BiometricAuthentication(Authentication):
    def __init__(self, stored_fingerprint_hash):
        self.stored_fingerprint_hash = stored_fingerprint_hash

    def authenticate(self, credentials):
        scanned_hash = credentials.get("fingerprint_hash")
        if scanned_hash == self.stored_fingerprint_hash:
            return True, "Biometric fingerprint match confirmed."
        return False, "Biometric scan mismatch."


def login_user(auth_service: Authentication, credentials: dict):
    success, msg = auth_service.authenticate(credentials)
    status = "SUCCESS" if success else "FAILED"
    print(f"[{auth_service.__class__.__name__}] Login {status}: {msg}")
    return success


auth_methods = [
    (PasswordAuthentication("shreya_m", "SecurePass@123"), {"username": "shreya_m", "password": "SecurePass@123"}),
    (OTPAuthentication("+91-9876543210", "492015"), {"mobile": "+91-9876543210", "otp": "492015"}),
    (BiometricAuthentication("SHA256_FINGERPRINT_HASH_A89F"), {"fingerprint_hash": "SHA256_FINGERPRINT_HASH_A89F"})
]

print("Multi-Factor Authentication Pipeline")
for auth_service, creds in auth_methods:
    login_user(auth_service, creds)
