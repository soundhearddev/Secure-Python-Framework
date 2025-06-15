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
spy.sm(mapping, file)

# Pattern anzeigen
print("Pattern (Mapping):")
for k, v in mapping.items():
    print(f"{repr(k)} -> {repr(v)}")
print("-" * 40)

# Datei verschlüsseln
spy.ef(file, mapping)
print(f"{file} wurde verschlüsselt.")