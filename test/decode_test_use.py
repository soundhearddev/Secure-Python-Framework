import os
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import secure_python.secure_python as spy

# Konfiguration
PASSWORD = "1234"
PY_FILE = "test_file.py"
SECURE_PATH = spy.sp()
ENC_PATH = SECURE_PATH + PY_FILE.removesuffix(".py") + ".json.enc"
ENCODED_PATH = SECURE_PATH + "data/" + PY_FILE.removesuffix(".py") + ".lpyip"

# 1. Mapping entschlüsseln
def load_encrypted_mapping(path, password):
    data = open(path, "rb").read()
    salt, nonce, tag, ct = data[:16], data[16:32], data[32:48], data[48:]
    key = PBKDF2(password, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plain = cipher.decrypt_and_verify(ct, tag)
    raw_map = json.loads(plain.decode("utf-8"))
    return {spy.k2z(k): v for k, v in raw_map.items()}

# 2. Datei dekodieren und ausführen
def decode_and_run(file_path, mapping):
    with open(file_path, "r", encoding="utf-8") as f:
        encoded = f.read()
    rev_map = {v: k for k, v in mapping.items()}
    decoded = ''.join(rev_map.get(c, '?') for c in encoded)
    exec(decoded)

if __name__ == "__main__":
    mapping = load_encrypted_mapping(ENC_PATH, PASSWORD)
    decode_and_run(ENCODED_PATH, mapping)
