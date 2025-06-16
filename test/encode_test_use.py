
import os
import json
import secure_python.secure_python as spy
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

PY_FILE      = "test_file.py"
PASSWORD    = "mein_geheimes_passwort"
JSON_PATH    = spy.sp() + PY_FILE.removesuffix(".py") + ".json"
MAPPING_ENC  = JSON_PATH + ".enc"

def print_mapping_info(mapping, label):
    print(f"\n[{label}] Mapping enthält {len(mapping)} Einträge.")
    example = list(mapping.items())[:10]
    print(f"Beispiel-Einträge: {example}")
    # Check auf ungültige Zeichen oder Mehrzeichen-Keys/Values
    errors = False
    for k, v in mapping.items():
        if not isinstance(k, str) or not isinstance(v, str):
            print(f"  ❌ Ungültiger Eintrag (kein str): {repr(k)} -> {repr(v)}")
            errors = True
        if len(k) != 1 or len(v) != 1:
            print(f"  ⚠️  Unerwartete Länge: {repr(k)} -> {repr(v)}")
            errors = True
    if not errors:
        print("  ✅ Alle Keys und Values sind einzelne Strings.")

# 1) Mapping erzeugen und als JSON speichern (mit UTF-8 & ensure_ascii=False!)

file = "test_file.py"

import secure_python as spy

# Debugging: Zeige alle Attribute des Moduls
print("Module attributes:", dir(spy))

# Debugging: Zeige den Pfad des Moduls
print("Module path:", spy.__file__)

# Versuche, die Funktion crm zu verwenden
try:
    mapping = spy.crm()
except AttributeError as e:
    print("ERROR:", e)


# Neues Pattern erzeugen und speichern
print(dir(spy))

mapping = spy.crm()
spy.sm(mapping, PY_FILE)
print(f"[+] Mapping als JSON geschrieben → {JSON_PATH}")

# 2) Mapping prüfen (vor Verschlüsselung)
print_mapping_info(mapping, "Vor Verschlüsselung")

# Pattern anzeigen
print("Pattern (Mapping):")
for k, v in mapping.items():
    print(f"{repr(k)} -> {repr(v)}")
print("-" * 40)


# 3) JSON-Datei verschlüsseln (AES-GCM)
def encrypt_file(in_path, out_path, password):
    data = open(in_path, "rb").read()
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(data)
    with open(out_path, "wb") as f:
        f.write(salt + cipher.nonce + tag + ct)
    print(f"[+] JSON verschlüsselt → {out_path}")

encrypt_file(JSON_PATH, MAPPING_ENC, PASSWORD)

# 4) Original JSON löschen
#os.remove(JSON_PATH)
print(f"[+] Original-JSON gelöscht")

# 5) Python-Datei per Mapping verschlüsseln (Keilschrift)
spy.ef(PY_FILE, mapping)
print(f"[+] {PY_FILE} per Keilschrift-Mapping verschlüsselt")

print("[+] Encoding + Verschlüsselung abgeschlossen.\n")
