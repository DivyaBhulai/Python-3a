g = int(input("Vul een getal in "))
nummers = {}

def generator():
    for i in range(1, g + 1):
        x = i*i
        nummers[i] = x
    print(nummers)
    
generator()

