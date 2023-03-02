"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Brejcha
email: brmast@seznam.cz
discord: Martin B.#5188
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

print("textovy analyzator")
jmeno = input("username:")
heslo = input("password:")
print("-"*43)              
if uzivatele.get(jmeno) != heslo:
    print("unregistered user, terminating the program.")
    quit()
print(f"""Welcome to the app, {jmeno}
We have 3 texts to be analyzed.""")
print("-"*43)
vyber = int(input("Enter a number btw 1 and 3 to select:"))
if vyber not in (1,2,3):
    print("wrong number, terminating the program.")
    quit()
print("-"*43)

TEXT = TEXTS[vyber-1]
SLOVA = TEXT.replace(".","").replace(",","").replace("\n"," ").replace("-"," ").split(" ")

POCET_SLOV = 0
POCET_SLOV_ZVP = 0
POCET_SLOV_PVP = 0
POCET_SLOV_PMP = 0
POCET_CISEL = 0
SUMA_CISEL = 0
cetnost = list()

for poradi, SLOVO in enumerate(SLOVA):
    if SLOVO:
        POCET_SLOV = POCET_SLOV + 1
        if SLOVO.isalpha():
            if SLOVO.istitle():
                POCET_SLOV_ZVP = POCET_SLOV_ZVP + 1
            if SLOVO.isupper():
                POCET_SLOV_PVP = POCET_SLOV_PVP + 1
            if SLOVO.islower():
                POCET_SLOV_PMP = POCET_SLOV_PMP + 1
        if SLOVO.isnumeric():
            POCET_CISEL = POCET_CISEL + 1
            SUMA_CISEL = SUMA_CISEL + int(SLOVO)
        cetnost.append(len(SLOVO))

print(f"""There are {POCET_SLOV} in the selected text. 
There are {POCET_SLOV_ZVP} titlecase words. 
There are {POCET_SLOV_PVP} uppercase words. 
There are {POCET_SLOV_PMP} lowercase words. 
There are {POCET_CISEL} numeric strings. 
The sum of all the numbers {SUMA_CISEL}""")
print("-"*43)
print("LEN\t|\tOCCURENCES\t|\tNR.")
print("-"*43)

for num in range(min(cetnost),max(cetnost)+1):
    znak = "*" * cetnost.count(num) + " " * (18 - cetnost.count(num))
    print(f"{num}\t|{znak}\t|\t{cetnost.count(num)}")
