# encrypt_config.py
import json
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_config(config, key):
    cipher_suite = Fernet(key)
    config_str = json.dumps(config).encode()

    encrypted_data = cipher_suite.encrypt(config_str)

    with open('configs/config.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

if __name__ == "__main__":
    key = "PSD1LpXi3H77JX7B5_dcm29sjXcmN5fDa5tgnEP8ySg="

    game_config = {
        "fps": 72,
        "width": 1400,
        "height": 800,
    }

    encrypt_config(game_config, key)
