producten = {"brood": "2", "sap": "3", "pizza": "5", "melk": "2", "mayonaise": "1"}
totaal = 0
import datetime
'''
def keuze():
    kiezen = input("Wil je het keuzemenu zien? Kies ja of nee ")
    if(kiezen == "ja"):
        
    if(kiezen == "nee"):
        exit()
    else:
        print("Je hebt iets anders dan ja of nee ingevuld")
'''
def optie_1(p):
    print("Zie rechts de producten met daarnaast hun prijs.")
    print(p)
    
def optie_2():
    product = input("Typ het product wat je wilt toevoegen. ")
    if(product in producten):
        print("Dit product staat al in de lijst.")
    prijs = input("Typ de prijs van het product ")
    producten[product] = prijs
    print("Het product is toegevoegd.")
    print(producten)
    return producten
    
def optie_3():
    product_2 = input("Typ het product wat je wilt verwijderen. ")
    if(product_2 in producten):
        del producten[product_2]
        print(producten)
    print("Dit product staat niet in de lijst.")
    
def optie_4():
    product_3 = input("Typ het product wat je wilt wijzigen. ")
    if(product_3 in producten):
        prijs_3 = input("Typ de prijs van het product ")
        producten[product_3] = prijs_3
        print("Het product is gewijzigd.")
        print(producten)
    else:
        print("Het product staat niet in de lijst.")
        print("Kies optie 2 om het product toe te voegen.")
        
def optie_5(p):
    print(p)
    totaal = 0
    aantal = int(input("Hoeveel verschillende producten wil je kopen? "))
    for i in range(aantal):
        if(i != aantal + 1):
            kopen = input("Typ 1 product ")
            if(kopen in p):
                d = p.get(kopen) 
                #print(d)
                hoeveel = int(input("Hoeveel wil je van het product kopen? "))
                y = int(hoeveel*int(d))
                totaal = totaal + y
            else:
                print("Dit product staat niet in de lijst.")
                print("Kies optie 2 om het product toe te voegen.")
                return totaal
        else:
            return totaal
    print("Je moet €", totaal, "betalen")
    return totaal
    #print("in functie :" + totaal)
    #return totaal
    
def optie_6(p):
    #print("yes")
    q = datetime.datetime.now()
    f = open("save.txt", "a")
    f.write(str(q))
    f.write("////")
    f.write(" dit zijn de producten ")
    f.write(str(p))
    #f.write(" dit is de totale prijs ")
    #f.write(str(t))
    f.write("\\\\")
    f.close()
    f = open("save.txt", "r")
    print(f.read())
    return

invoer = input("Wil je het keuzemenu zien? ")
while invoer == "ja":
#global totaal
    print("1. Bekijk alle producten.")
    print("2. Voeg een product toe.")
    print("3. Verwijder een product.")
    print("4. Wijzig een product.")
    print("5. Boodschappen doen.")
    print("6. Sla producten op.")
    kies = input("Kies een optie ")
    
    if(kies == "1"):
        optie_1(producten)
    if(kies == "2"):
        optie_2()
    if(kies == "3"):
        optie_3()
    if(kies == "4"):
        optie_4()
    if(kies == "5"):
        totaal = optie_5(producten)
    if(kies == "6"):
        #print(totaal)
        optie_6(producten)
    #else:
        #print("Je hebt iets verkeerds ingevuld.")
