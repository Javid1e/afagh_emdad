import random


def generate_otp():
    return str(random.randint(100000, 999999))


def verify_otp(user_otp, otp):
    return user_otp == otp
