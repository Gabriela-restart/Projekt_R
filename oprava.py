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

jmena = ["bob" , "ann", "mike" , "liz"]
hesla = ["123" , "pass123", "password123","pass123"]
uzivatele = dict(zip(jmena, hesla))
cisla_textu = (1, 2, 3)
oddelovac = "-"*48

# print(type(TEXTS)) typ je list
# print(cisla_textu)

text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2] 
# print(type(text_1)) typ je str

slova_1 =text_1.split() 
slova_2 =text_2.split()
slova_3 =text_3.split()
# print(text_1)

velka_pismena = 0
vycistena_slova = [] # list
slova_velkym = 0
slova_malym = 0
pocet_cisel = 0
suma_cisel = [] # list
pocet_pismen = {}
cetnost_delky = {}


# jmeno_a_heslo = {"bob" : "123", "ann":"pass123", "mike":"password123","liz":"pass123"}
# print(uzivatele)

# 1. Vyžádá si od uživatele přihlašovací jméno a heslo,
uzivatel = input("uživatelské jméno:") 
heslo = input ("heslo:")


if uzivatel in uzivatele and uzivatele [uzivatel] == heslo: # 2. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
    print(oddelovac)
    print("Vítej v programu,", uzivatel)  # 3. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
    print("Máme 3 texty k analýze.") 
    print(oddelovac)
    cislo_textu = (input("Zadej číslo mezi 1 a 3 pro výběr: ")) # 5. Program nechá uživatele vybrat mezi třemi texty uloženými v  proměnné TEXTS
    print(oddelovac)

    if not cislo_textu.isdigit():
      print("Nebylo zadáno číslo") # 7. pokud uživatel zadá jiný vstup než číslo, program ž upozorní a skončí.
      quit()

    cislo_textu_1 = int(cislo_textu)

    if cislo_textu_1 not in cisla_textu:      # 6. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí, 
      print("Zadané číslo textu není k dispozici") 
      quit()
    
    else:    
      if cislo_textu_1 == 1: 
        # print(text_1) #  Spočítá následujícíc statistiky :
        for slovo in slova_1:           
            ciste_slova = slovo.strip(' .,!?')
            vycistena_slova.append(ciste_slova)        
        print("V textu je", len(vycistena_slova), "slov.") # 8. počet slov,
        
        for slovo in slova_1:          
            if slovo.istitle():
                velka_pismena +=1
        print("V textu je", velka_pismena, "slov začínajících velkým písmenem.") # 9. počet slov začínajících velkým písmenem,

        for slovo in slova_1:           
            if slovo.isupper():
                slova_velkym +=1
        print("V textu je", slova_velkym, "slov psaných velkými písmeny.") # 10. počet slov psaných velkými písmeny,

        for slovo in slova_1:           
            if slovo.islower():
                slova_malym +=1
        print("V textu je", slova_malym, "slov psaných malými písmeny.") # 11. počet slov psaných malými písmeny,

        for slovo in slova_1:          
            if slovo.isdigit() :
                pocet_cisel +=1
        print("V textu je", pocet_cisel," počet čísel.") # 12. počet čísel (ne cifer),
        
        for slovo in slova_1:         
            if slovo.isdigit() :
                suma_cisel.append(int(slovo))
                vysledek = sum(suma_cisel)
        print("Suma všech čísel v textu je", vysledek) # 13. sumu všech čísel (ne cifer) v textu.,
        print(oddelovac)

        print("LEN|  OCCURRENCES  |NR.") 
        print(oddelovac)

        for slovo in slova_1:
            ciste_slova = slovo.strip(' .,!?')
            delka = len(ciste_slova)             
            if delka not in cetnost_delky:
                cetnost_delky[delka] = 1
            else:
                cetnost_delky[delka]=  cetnost_delky[delka] + 1
        setrizeno = sorted(cetnost_delky.items())                      
        for key, value in setrizeno: 
            print("{:>2} | {:<17}| {:<3}".format(key, "*" * value, value))
        print() 


      if cislo_textu_1 == 2: 

        for slovo in slova_2:
            ciste_slova = slovo.strip(' .,!?')
            vycistena_slova.append(ciste_slova)
        print("V textu je", len(vycistena_slova), "slov.") 

        for slovo in slova_2:          
            if slovo.istitle():
                velka_pismena +=1
        print("V textu je", velka_pismena, "slov začínajících velkým písmenem.")

        for slovo in slova_2:         
            if slovo.isupper():
                slova_velkym +=1
        print("V textu je", slova_velkym, "slov psaných velkými písmeny.") 

        for slovo in slova_2:           
            if slovo.islower():
                slova_malym +=1
        print("V textu je", slova_malym, "slov psaných malými písmeny.") 

        for slovo in slova_2:          
            if slovo.isdigit() :
                pocet_cisel +=1
        print("V textu je", pocet_cisel," počet čísel.")
        
        for slovo in slova_2:      
            if slovo.isdigit() :
                suma_cisel.append(int(slovo))
                vysledek = sum(suma_cisel)
        print("Suma všech čísel v textu je", vysledek)
        print(oddelovac)

        print("LEN|  OCCURRENCES  |NR.") 
        print(oddelovac)

        for slovo in slova_2:  
            ciste_slova = slovo.strip(' .,!?')
            delka = len(ciste_slova)             
            if delka not in cetnost_delky:
                cetnost_delky[delka] = 1
            else:
                cetnost_delky[delka]=  cetnost_delky[delka] + 1
        setrizeno = sorted(cetnost_delky.items())                      
        for key, value in setrizeno:          
            print("{:>2} | {:<17}| {:<3}".format(key, "*" * value, value))
        print() 


      if cislo_textu_1 == 3: 

        for slovo in slova_3:          
            ciste_slova = slovo.strip(' .,!?\n\t')
            vycistena_slova.append(ciste_slova)
        print("V textu je", len(vycistena_slova), "slov.")
        
        for slovo in slova_3: 
            if slovo.istitle():
                velka_pismena +=1
        print("V textu je", velka_pismena, "slov začínajících velkým písmenem.") 

        for slovo in slova_3:
            if slovo.isupper():
                slova_velkym +=1
        print("V textu je", slova_velkym, "slov psaných velkými písmeny.") 

        for slovo in slova_3:      
            if slovo.islower():
                slova_malym +=1
        print("V textu je", slova_malym, "slov psaných malými písmeny.") 

        for slovo in slova_3:           
            if slovo.isdigit() :
                pocet_cisel +=1
        print("V textu je", pocet_cisel," počet čísel.") 
        
        for slovo in slova_3:            
            if slovo.isdigit() :
                suma_cisel.append(int(slovo))
                vysledek = sum(suma_cisel)
        print("Suma všech čísel v textu je", vysledek) 
        print(oddelovac)
  
        print("LEN|  OCCURRENCES  |NR.") 
        print(oddelovac)

        for slovo in slova_3:  
            ciste_slova = slovo.strip(' .,!?')
            delka = len(ciste_slova)             
            if delka not in cetnost_delky:
                cetnost_delky[delka] = 1
            else:
                cetnost_delky[delka]=  cetnost_delky[delka] + 1            
        setrizeno = sorted(cetnost_delky.items())                      
        for key, value in setrizeno:          
            print("{:>2} | {:<17}| {:<3}".format(key, "*" * value, value))
        print() 
 
else:
    print("neregistrovaný uživatel, ukončuji program..")
    print() 
    quit()