fruit = {"0": "meloen", "1": "aardbei", "2": "appel"}

#print("Naar welke key zoek je? Key ")
x = input("Naar welke key zoek je? Key ")

def zoeken():
    if x in fruit:
        return True
    else:
        return False
    
    
print(zoeken())
        

