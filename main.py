"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Gabriela Hořínková
email: gabriela.lostakova@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

jmena = ["bob", "ann", "mike", "liz"]
hesla = ["123", "pass123", "password123", "pass123"]
uzivatele = dict(zip(jmena, hesla))
cisla_textu = list(range(1, len(TEXTS) + 1))

oddelovac = "-" * 48

uzivatel = input("uživatelské jméno:") # 1. Vyžádá si od uživatele přihlašovací jméno a heslo
heslo = input("heslo:")

if uzivatel in uzivatele and uzivatele[uzivatel] == heslo: # 2. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
    print(oddelovac)
    print("Vítej v programu,", uzivatel)  # 3. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print("Máme",len(TEXTS),"texty k analýze.")
    print(oddelovac)
    cislo_textu = input(f"Zadej číslo mezi {min(cisla_textu)} a {max(cisla_textu)} pro výběr: ") # 5. Program nechá uživatele vybrat mezi třemi texty uloženými v  proměnné TEXTS
    print(oddelovac)

    if not cislo_textu.isdigit():
        print("Nebylo zadáno číslo") # 7. pokud uživatel zadá jiný vstup než číslo, program upozorní a skončí
        print()
        quit()

    cislo_textu_int = int(cislo_textu)

    if cislo_textu_int not in cisla_textu: # 6 Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
        print("Zadané číslo textu není k dispozici")
        print()
        quit()

    else:

        for index, analyzovany_text in enumerate(TEXTS, start=1):  # print(f"{index}. {analyzovany_text}")

            if cislo_textu_int == index:

                jednotliva_slova = analyzovany_text.split()
                cista_slova = [slovo.strip(".,!?;:-_'\"()[]{}") for slovo in jednotliva_slova]
                velka_pismena = 0
                slova_velkym = 0
                slova_malym = 0
                pocet_cisel = 0
                suma_cisel = []
                soucet = 0
                delka = 0
                cetnost_delky = {}

                for slovo in cista_slova:
                    if slovo.istitle():
                        velka_pismena += 1

                    if slovo.isupper():
                        slova_velkym +=1

                    if slovo.islower():
                        slova_malym += 1

                    if slovo.isdigit():
                        pocet_cisel += 1
                        suma_cisel.append(int(slovo))
                soucet = sum(suma_cisel)

                print(f"V textu je {len(cista_slova)} slov.") # 8. počet slov
                print(f"V textu je {velka_pismena} slov začínajících velkým písmenem.") # 9. počet slov začínajících velkým písmenem
                print(f"V textu je {slova_velkym} slov psaných velkými písmeny.") # 10. počet slov psaných velkými písmeny
                print(f"V textu je {slova_malym} slov psaných malými písmeny.") # 11. počet slov psaných malými písmeny
                print(f"V textu je {pocet_cisel} počet čísel.") # 12. počet čísel (ne cifer)
                print(f"Suma všech čísel v textu je {soucet}." ) # 13. sumu všech čísel (ne cifer) v textu
                print(oddelovac)
                print("LEN|  OCCURRENCES  |NR.")
                print(oddelovac)

                for slovo in cista_slova:
                    delka = len(slovo)
                    if delka not in cetnost_delky:
                        cetnost_delky[delka] = 1
                    else:
                        cetnost_delky[delka] = cetnost_delky[delka] + 1

                setrizeno = sorted(cetnost_delky.items())
                for key, value in setrizeno:
                    print(f"{key:>2} | {'*' * value:<17} | {value:<3}")

        print()
else:
    print("neregistrovaný uživatel, ukončuji program..")
    print()
    quit()