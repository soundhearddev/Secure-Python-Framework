
f = "test_file.py"
import secure_python.secure_python as spy

# Entschlüsselung
m = spy.lm(f)
dc = spy.dfts(f, m)


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
