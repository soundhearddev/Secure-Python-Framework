import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import secure_python.secure_python as spy

# Konfiguration
PY_FILE = "test_file.py"
PASSWORD = "1234"
JSON_PATH = spy.sp() + PY_FILE.removesuffix(".py") + ".json"
ENC_PATH = JSON_PATH + ".enc"

# 1. Mapping generieren und speichern
mapping = spy.crm()
spy.sm(mapping, PY_FILE)
print(f"[+] Mapping gespeichert → {JSON_PATH}")

# 2. JSON-Datei AES-verschlüsseln
def encrypt_file(in_path, out_path, password):
    data = open(in_path, "rb").read()
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(data)
    with open(out_path, "wb") as f:
        f.write(salt + cipher.nonce + tag + ct)
    print(f"[+] Verschlüsselt → {out_path}")

encrypt_file(JSON_PATH, ENC_PATH, PASSWORD)

# 3. Optional: Original-JSON löschen
os.remove(JSON_PATH)

# 4. Datei verschlüsseln mit Mapping
spy.ef(PY_FILE, mapping)
print(f"[+] {PY_FILE} verschlüsselt mit Mapping.")
