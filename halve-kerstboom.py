letters = ["h", "e", "l", "l", "o"]
def functie(letters):
    z = len(letters)
    #print(z)
    for i in range(z + 1):   
        x = letters[-1 + i]
        print(x * i)
    
functie(letters)