 #"""
#projekt_1.py: první projekt do Engeto Online Python Akademie
#author: Lucie Geigerová
#email: luciegeigerova@seznam.cz
#discord: Lucie #2344
#"""

 # slovnik se jmeny uzivatelu a hesly
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# zadani prihlasovaciho jmena a hesla uzivatelem
username = input("USERNAME:")                 # moje pozn. muzu pouzit i metodu .isupper()
password = input("PASSWORD:")
sep = 44 * ("-")
print(sep)

# podminky prihlaseni uzivatele
if users.get(username) == password:           # overi ze zadane jmeno a heslo k sobe patri, pokud ne ukonci se
    print("Welcome to the app", username.capitalize(), "!", "\nWe have 3 texts to be analyzed.")

else:
    print("Unregistered user, terminating the program...")
    quit()

print(sep)

# promenna texty
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

# vyber textu uzivatelem
select = input("Enter a number btw. 1 to 3 to select text:")

# podminky vyberu textu uzivatelem
if select.isdigit() and int(select) in range(1,4):         # overi ze vyber je ciselny a v danem rozsahu
    print(sep)

else:
    print(sep, "\nYou can choose number just from 1-3, terminatig program...")
    quit()

# POCITANI STATISTIK
select = int(select) - 1                     # vyber uzivatele - 1, protoze list indexuje od 0
sel_text = TEXTS[select]                     # promenna vybraneho textu

#print(TEXTS[select]) - moje pozn. pro overeni spravnosti zvoleneho textu

# 1) pocet slov v textu
words_count = len(sel_text.split())          # split rozdeli text na zaklade mezer a spocita delku pomoci fce len
print("There are", words_count, "words in the selected text.")

# 2) promenna pocet slov zacinajicich velkym pismenem
title_words = 0
# 3) promenna pocet slov velkymi pismeny
upper_words = 0
# 4) promenna pocet slov malymi pismeny
lower_words = 0
# 5) promenna pocet ciselnzch slov v textu
numeric_words = 0
# pomocna promenna s listem pro scitani cisel
l_num_words = list()
# 6) promenna se souctem cisel
numbers_sum = 0

# smycka s podminkami k hledani a scitani slov v textu
for word in sel_text.split():
    if word.istitle():                  # slova s velkym pocatecnim pismenem
        title_words += 1
    elif word.isupper():                # slova velkymi pismeny
        upper_words += 1
    elif word.islower():                # slova malymi pismeny
        lower_words += 1
    elif word.isnumeric():
        numeric_words += 1              # pokud je slovo numericke - secti pocet techto slov
        l_num_words.append(int(word))   # a zaroven numericka slova pridej do listu l_num_words a udelej z nich int

# soucet vsech cisel z vytvoreneho listu
for number in l_num_words:
    numbers_sum += int(number)          # z numer.slova udelej int a pridej jej do promenne numbers_sum, kde je secti

# VYSTUPY SMYCKY
print("There are", title_words, "titlecase words.")
print("There are", upper_words, "uppercase words.")
print("There are", lower_words, "lowercase words.")
print("There are", numeric_words, "numeric words.")
print("The sum of all numbers is", numbers_sum, ".")

print(sep)

# GRAF
occurences = dict()                # slovnik pro delky slov

for word in sel_text.split():
    word = word.strip(",.;:")      # slovo ocisti od znaku ,.:; metodou strip
    length = len(word)             # promenna pro delku slova, delka slova se urci pomoci fce len
    if length not in occurences:
        occurences[length] = 0
    occurences[length] += 1        # pro klic pouzijeme []

occurences_sorted = dict(sorted(zip(occurences.keys(), occurences.values())))   # fce sorted seradi slovnik vzestupne

# vystup - graf
print("LEN|     OCCURENCES     |NR.")
print(sep)

for key, value in enumerate(occurences_sorted.values()):
    print(f"{(key + 1):3}| {('*' * value):18} |{value}")






