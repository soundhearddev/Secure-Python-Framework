import os
import json
import secure_python.secure_python as spy
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


f = "test_file.py"
import secure_python.secure_python as spy

# Entschlüsselung
m = spy.lm(f)
dc = spy.dfts(f, m)

PASSWORD = "mein_geheimes_passwort"
PY_FILE = "test_file.py"

def secure_pfad():
    # Nutze deine Funktion aus spy oder definiere passend
    return spy.sp()

# Pfade
json_path = secure_pfad() + PY_FILE.removesuffix(".py") + ".lpyip.json"
enc_path = json_path + ".enc"

def print_mapping_info(mapping, label):
    print(f"\n[{label}] Mapping enthält {len(mapping)} Einträge.")
    example = list(mapping.items())[:10]
    print(f"Beispiel-Einträge: {example}")
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

def save_mapping_and_encrypt():
    # 1) Mapping erzeugen
    mapping = spy.crm()
    print_mapping_info(mapping, "Mapping vor Speicherung")

    # 2) Mapping als JSON speichern
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False)
    print(f"[+] Mapping als JSON gespeichert unter: {json_path}")

    # 3) JSON lesen und in bytes umwandeln (UTF-8)
    with open(json_path, "rb") as f:
        data = f.read()
    print(f"[+] JSON-Daten Größe in Bytes vor Verschlüsselung: {len(data)}")

    # 4) AES-GCM verschlüsseln
    salt = get_random_bytes(16)
    key = PBKDF2(PASSWORD, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(data)

    # 5) Speichern: salt | nonce | tag | ciphertext (alles Bytes)
    with open(enc_path, "wb") as f:
        f.write(salt + cipher.nonce + tag + ct)
    print(f"[+] Mapping verschlüsselt und gespeichert unter: {enc_path}")

def decrypt_mapping():
    print(f"[+] Versuche Mapping-Datei zu entschlüsseln: {enc_path}")
    data = open(enc_path, "rb").read()
    salt = data[:16]
    nonce = data[16:32]
    tag = data[32:48]
    ct = data[48:]
    key = PBKDF2(PASSWORD, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plain = cipher.decrypt_and_verify(ct, tag)
    print(f"[+] Entschlüsselter JSON-String (erste 500 Zeichen): {plain[:500].decode('utf-8')}")
    verschl = json.loads(plain.decode("utf-8"))
    # k2z zurückwandeln
    mapping = {spy.k2z(k): v for k, v in verschl.items()}
    print_mapping_info(mapping, "Nach Entschlüsselung")
    return mapping

def encode_script(mapping):
    # Per Mapping das Script in Keilschrift verschlüsseln und speichern
    spy.ef(PY_FILE, mapping)
    print(f"[+] {PY_FILE} per Keilschrift verschlüsselt.")

def check_and_decode(mapping):
    encoded_file_path = secure_pfad() + "data\\" + PY_FILE.removesuffix(".py") + ".lpyip"
    if not os.path.exists(encoded_file_path):
        raise FileNotFoundError(f"Verschlüsselte Datei nicht gefunden: {encoded_file_path}")

    with open(encoded_file_path, "r", encoding="utf-8") as f:
        encoded_code = f.read()
    print(f"[+] Eingelesene verschlüsselte Script-Datei hat {len(encoded_code)} Zeichen.")

    reverse_mapping = {v: k for k, v in mapping.items()}
    missing_chars = set(c for c in encoded_code if c not in reverse_mapping)

    if missing_chars:
        print(f"❗ Fehlende Zeichen im Mapping, die nicht entschlüsselt werden können: {missing_chars}")
    else:
        print("✅ Alle Zeichen im verschlüsselten Script sind im Mapping vorhanden.")

    decoded_code = ''.join(reverse_mapping.get(c, '?') for c in encoded_code)
    unknown_count = decoded_code.count('?')
    if unknown_count > 0:
        print(f"⚠️ Es wurden {unknown_count} unbekannte Zeichen beim Entschlüsseln gefunden.")

    print("[+] Entschlüsselter Script-Code (Ausgabe gekürzt):")
    print(decoded_code[:500])

    print("\n[+] Starte Script-Ausführung...\n")
    exec(decoded_code)

if __name__ == "__main__":
    save_mapping_and_encrypt()
    mapping = decrypt_mapping()
    encode_script(mapping)
    check_and_decode(mapping)

#print("Entschlüsselter Code:")
#print(dc)

# Überprüfen, ob der entschlüsselte Code gültig ist
try:
    exec(dc)
except SyntaxError as e:
    print(f"❌ SyntaxError im entschlüsselten Code: {e}")
except Exception as e:
    print(f"❌ Fehler beim Ausführen des entschlüsselten Codes: {e}")

#or in short:
#f = "test_file.py";import secure_python.secure_python as spy;m = spy.lm(f);dc = spy.dfts(f, m);exec(dc)
