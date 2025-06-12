from secure_python.secure_python import crm, et, dt, z2k, k2z

# Beispieltext
text = "Hallo, Welt!"

# Erstelle ein zufälliges Mapping
mapping = crm()

# Text verschlüsseln (encode)
encoded = et(text, mapping)
print("Verschlüsselt:", encoded)

# Text entschlüsseln (decode)
decoded = dt(encoded, mapping)
print("Entschlüsselt:", decoded)

# Zeichen zu Keilschrift
keilschrift = z2k(text)
print("Keilschrift:", keilschrift)

# Keilschrift zurück zu Zeichen
zeichen = k2z(keilschrift)
print("Zeichen:", zeichen)