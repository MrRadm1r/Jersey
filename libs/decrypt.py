import json
from typing import Any
from cryptography.fernet import Fernet

def decrypt(encrypted_file, key, item_key) -> Any:
    cipher_suite = Fernet(key)

    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    config = json.loads(decrypted_data)
    return config[item_key]

if __name__ == "__main__":
    key = input()
    decrypted_config = decrypt('configs/config.encrypted', key, "fps")

    print("Decrypted Config:")
    print(decrypted_config)
