import json
import random
from importlib import resources
# Alle Zeichen, die im Python-Code vorkommen können (inkl. Zeilenumbruch und Tab)
z = (
    [chr(i) for i in range(32, 127)]  # Standard-ASCII-Zeichen
    + ['\n', '\t', 'ü', 'ä', 'ö', 'ß']                    # Zeilenumbruch und Tab
)

# Keilschriftzeichen (mindestens so viele wie Zeichen!)
k = list("𒀀𒀁𒀂𒀃𒀄𒀅𒀆𒀇𒀈𒀉𒀊𒀋𒀌𒀍𒀎𒀏𒀐𒀑𒀒𒀓𒀔𒀕𒀖𒀗𒀘𒀙𒀚𒀛𒀜𒀝𒀞𒀟𒀠𒀡𒀢𒀣𒀤𒀥𒀦𒀧𒀨𒀩𒀪𒀫𒀬𒀭𒀮𒀯𒀰𒀱𒀲𒀳𒀴𒀵𒀶𒀷𒀸𒀹𒀺𒀻𒀼𒀽𒀾𒀿𒁀𒁁𒁂𒁃𒁄𒁅𒁆𒁇𒁈𒁉𒁊𒁋𒁌𒁍𒁎𒁏𒁐𒁑𒁒𒁓𒁔𒁕𒁖𒁗𒁘𒁙𒁚𒁛𒁜𒁝𒁞𒁟𒁠𒁡𒁢𒁣𒁤𒁥𒁦𒁧𒁨𒁩𒁪𒁫𒁬𒁭𒁮𒁯𒁰𒁱𒁲𒁳𒁴𒁵𒁶𒁷𒁸𒁹𒁺𒁻𒁼𒁽𒁾𒁿𒂀𒂁𒂂𒂃𒂄𒂅𒂆𒂇𒂈𒂉𒂊𒂋𒂌𒂍𒂎𒂏𒂐𒂑𒂒𒂓𒂔𒂕𒂖𒂗𒂘𒂙𒂚𒂛𒂜𒂝𒂞𒂟𒂠𒂡𒂢𒂣𒂤𒂥𒂦𒂧𒂨𒂩𒂪𒂫𒂬𒂭𒂮𒂯𒂰𒂱𒂲𒂳𒂴𒂵𒂶𒂷𒂸𒂹𒂺𒂻𒂼𒂽𒂾𒂿𒃀𒃁𒃂𒃃𒃄𒃅𒃆𒃇𒃈𒃉𒃊𒃋𒃌𒃍𒃎𒃏𒃐𒃑𒃒𒃓𒃔𒃕𒃖𒃗𒃘𒃙𒃚𒃛𒃜𒃝𒃞𒃟𒃠𒃡𒃢𒃣𒃤𒃥𒃦𒃧𒃨𒃩𒃪𒃫𒃬𒃭𒃮𒃯𒃰𒃱𒃲𒃳𒃴𒃵𒃶𒃷𒃸𒃹𒃺𒃻𒃼𒃽𒃾𒃿𒄀𒄁𒄂𒄃𒄄𒄅𒄆𒄇𒄈𒄉𒄊𒄋𒄌𒄍𒄎𒄏𒄐𒄑𒄒𒄓𒄔𒄕𒄖𒄗𒄘𒄙𒄚𒄛𒄜𒄝𒄞𒄟𒄠𒄡𒄢𒄣𒄤𒄥𒄦𒄧𒄨𒄩𒄪𒄫𒄬𒄭𒄮𒄯𒄰𒄱𒄲𒄳𒄴𒄵𒄶𒄷𒄸𒄹𒄺𒄻𒄼𒄽𒄾𒄿𒅀𒅁𒅂𒅃𒅄𒅅𒅆𒅇𒅈𒅉𒅊𒅋𒅌𒅍𒅎𒅏𒅐𒅑𒅒𒅓𒅔𒅕𒅖𒅗𒅘𒅙𒅚𒅛𒅜𒅝𒅞𒅟𒅠𒅡𒅢𒅣𒅤𒅥𒅦𒅧𒅨𒅩𒅪𒅫𒅬𒅭𒅮𒅯𒅰𒅱𒅲𒅳𒅴𒅵𒅶𒅷𒅸𒅹𒅺𒅻𒅼𒅽𒅾𒅿𒆀𒆁𒆂𒆃𒆄𒆅𒆆𒆇𒆈𒆉𒆊𒆋𒆌𒆍𒆎𒆏𒆐𒆑𒆒𒆓𒆔𒆕𒆖𒆗𒆘𒆙𒆚𒆛𒆜𒆝𒆞𒆟𒆠𒆡𒆢𒆣𒆤𒆥𒆦𒆧𒆨𒆩𒆪𒆫𒆬𒆭𒆮𒆯𒆰𒆱𒆲𒆳𒆴𒆵𒆶𒆷𒆸𒆹𒆺𒆻𒆼𒆽𒆾𒆿𒇀𒇁𒇂𒇃𒇄𒇅𒇆𒇇𒇈𒇉𒇊𒇋𒇌𒇍𒇎𒇏𒇐𒇑𒇒𒇓𒇔𒇕𒇖𒇗𒇘𒇙𒇚𒇛𒇜𒇝𒇞𒇟𒇠𒇡𒇢𒇣𒇤𒇥𒇦𒇧𒇨𒇩𒇪𒇫𒇬𒇭𒇮𒇯𒇰𒇱𒇲𒇳𒇴𒇵𒇶𒇷𒇸𒇹𒇺𒇻𒇼𒇽𒇾𒇿𒈀𒈁𒈂𒈃𒈄𒈅𒈆𒈇𒈈𒈉𒈊𒈋𒈌𒈍𒈎𒈏𒈐𒈑𒈒𒈓𒈔𒈕𒈖𒈗𒈘𒈙𒈚𒈛𒈜𒈝𒈞𒈟𒈠𒈡𒈢𒈣𒈤𒈥𒈦𒈧𒈨𒈩𒈪𒈫𒈬𒈭𒈮𒈯𒈰𒈱𒈲𒈳𒈴𒈵𒈶𒈷𒈸𒈹𒈺𒈻𒈼𒈽𒈾𒈿𒉀𒉁𒉂𒉃𒉄𒉅𒉆𒉇𒉈𒉉𒉊𒉋𒉌𒉍𒉎𒉏𒉐𒉑𒉒𒉓𒉔𒉕𒉖𒉗𒉘𒉙𒉚𒉛𒉜𒉝𒉞𒉟𒉠𒉡𒉢𒉣𒉤𒉥𒉦𒉧𒉨𒉩𒉪𒉫𒉬𒉭𒉮𒉯𒉰𒉱𒉲𒉳𒉴𒉵𒉶𒉷𒉸𒉹𒉺𒉻𒉼𒉽𒉾𒉿𒊀𒊁𒊂𒊃𒊄𒊅𒊆𒊇𒊈𒊉𒊊𒊋𒊌𒊍𒊎𒊏𒊐𒊑𒊒𒊓𒊔𒊕𒊖𒊗𒊘𒊙𒊚𒊛𒊜𒊝𒊞𒊟𒊠𒊡𒊢𒊣𒊤𒊥𒊦𒊧𒊨𒊩𒊪𒊫𒊬𒊭𒊮𒊯𒊰𒊱𒊲𒊳𒊴𒊵𒊶𒊷𒊸𒊹𒊺𒊻𒊼𒊽𒊾𒊿𒋀𒋁𒋂𒋃𒋄𒋅𒋆𒋇𒋈𒋉𒋊𒋋𒋌𒋍𒋎𒋏𒋐𒋑𒋒𒋓𒋔𒋕𒋖𒋗𒋘𒋙𒋚𒋛𒋜𒋝𒋞𒋟𒋠𒋡𒋢𒋣𒋤𒋥𒋦𒋧𒋨𒋩𒋪𒋫𒋬𒋭𒋮𒋯𒋰𒋱𒋲𒋳𒋴𒋵𒋶𒋷𒋸𒋹𒋺𒋻𒋼𒋽𒋾𒋿𒌀𒌁𒌂𒌃𒌄𒌅𒌆𒌇𒌈𒌉𒌊𒌋𒌌𒌍𒌎𒌏𒌐𒌑𒌒𒌓𒌔𒌕𒌖𒌗𒌘𒌙𒌚𒌛𒌜𒌝𒌞𒌟𒌠𒌡𒌢𒌣𒌤𒌥𒌦𒌧𒌨𒌩𒌪𒌫𒌬𒌭𒌮𒌯𒌰𒌱𒌲𒌳𒌴𒌵𒌶𒌷𒌸𒌹𒌺𒌻𒌼𒌽𒌾𒌿𒍀𒍁𒍂𒍃𒍄𒍅𒍆𒍇𒍈𒍉𒍊𒍋𒍌𒍍𒍎𒍏𒍐𒍑𒍒𒍓𒍔𒍕𒍖𒍗𒍘𒍙𒍚𒍛𒍜𒍝𒍞𒍟𒍠𒍡𒍢𒍣𒍤𒍥𒍦𒍧𒍨𒍩𒍪𒍫𒍬𒍭𒍮𒍯𒍰𒍱𒍲𒍳𒍴𒍵𒍶𒍷𒍸𒍹𒍺𒍻𒍼𒍽𒍾𒍿𒎀𒎁𒎂𒎃𒎄𒎅𒎆𒎇𒎈𒎉𒎊𒎋𒎌𒎍𒎎𒎏𒎐𒎑𒎒𒎓𒎔𒎕𒎖𒎗𒎘𒎙")

def z2k(s):  # Zeichen zu Keilschrift
    return ''.join(k[z.index(c)] if c in z else '?' for c in s)

def k2z(s):  # Keilschrift zu Zeichen
    return ''.join(z[k.index(c)] if c in k else '?' for c in s)

def crm():  # Create random mapping
    shuffled = k[:]
    random.shuffle(shuffled)
    return {z[i]: shuffled[i] for i in range(len(z))}

def secure_pfad():
    path_str = str(resources.files("secure_python.secure"))
    if path_str.startswith("MultiplexedPath('") and path_str.endswith("')"):
        path_str = path_str[16:-2]
    return path_str

def sm(mapping, file):  # Save mapping
    verschleiert = {z2k(k): v for k, v in mapping.items()}
    filepath = secure_pfad() + file.removesuffix(".py") + ".lpip.json"
    print(filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(verschleiert, f, ensure_ascii=False)

def lm(file):  # Load mapping
    filepath = secure_pfad() + file.removesuffix(".py") + ".lpip.json"
    with open(filepath, "r", encoding="utf-8") as f:
        verschleiert = json.load(f)
    mapping = {k2z(k): v for k, v in verschleiert.items()}
    return mapping

def et(text, mapping):  # Encode text
    return ''.join(mapping.get(c, '?') for c in text)

def dt(text, mapping):  # Decode text
    reverse = {v: k for k, v in mapping.items()}
    return ''.join(reverse.get(c, '?') for c in text)



def ef(file, mapping): #encode file
    
    with open(file, "r", encoding="utf-8") as f:
        code = f.read()
    encoded = et(code, mapping)
    out_file = secure_pfad() + "\\data\\" + file.removesuffix(".py") + ".lpip"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(encoded)


def oef(file): #open encoded file
    file = secure_pfad() + "\\data\\" + file.removesuffix(".py") + ".lpip"
    with open(file, "r", encoding="utf-8") as f:
        encoded_code = f.read()
    return encoded_code


import os

import os

def df(file):  # decode file
    # Erstelle den Pfad zur verschlüsselten Datei
    file_path = secure_pfad() + "\\data\\" + file.removesuffix(".py") + ".lpip"
    
    # Überprüfe, ob die Datei existiert
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Die Datei {file_path} wurde nicht gefunden.")
    
    # Lade das Mapping
    mapping = lm(file)
    
    # Öffne die verschlüsselte Datei
    opened_file = oef(file)
    
    # Dekodiere den Inhalt
    decoded = dt(opened_file, mapping)
    
    # Speichere die dekodierte Datei als .py im aktuellen Arbeitsverzeichnis
    out_file = os.getcwd() + "\\" + file.removesuffix(".py") + ".py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(decoded)


def dfts(file, mapping): #decode file to string
    opened_file = oef(file)
    decoded = dt(opened_file, mapping)
    return decoded