kleuren = ["blauw", "groen", "paars"]
def toevoegen(x, y):
    del y[x]
    print(y)
    
#1 = index nummer van het item wat je wilt verwijderen
toevoegen(1, kleuren)