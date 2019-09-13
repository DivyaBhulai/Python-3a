kleuren = {1: "rood", 2: "blauw", 3: "groen"}
d = int(input("typ een key "))


def functie(k, key):
    del kleuren[key]
    print(kleuren)
    
    
functie(kleuren, d)