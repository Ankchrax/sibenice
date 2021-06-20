from random import randrange

seznam_slov = ("stromek","trávník","stavení")
slovo = seznam_slov[randrange(len(seznam_slov))]
chyby = 0
tajenka = "-" * len(slovo)

def obrazek(level):
    if level == 0:
        return """
        ~~~~~~~
        """
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """

def zamen (slovo,pismeno,pozice):
    zacatek = slovo[:pozice]
    konec = slovo[pozice+1:]
    nove_slovo = zacatek+pismeno+konec
    
    return nove_slovo

print(tajenka)
while tajenka != slovo:
    pismeno = input("Zadej písmeno: ")
    if pismeno in slovo:
        pozice = slovo.index(pismeno)
        tajenka = zamen(tajenka,pismeno,pozice)
        print(obrazek(chyby))
        print(tajenka)
    else:
        chyby += 1
        print("Máte ",chyby,"chybných odpovědí!")
        print(obrazek(chyby)) 
        if chyby == 9:
            print("Prohrál jsi!")
            break
        
        print(tajenka)
if tajenka == slovo:
    print("Gratuluji vyhrál jsi!")




