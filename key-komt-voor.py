fruit = {"0": "meloen", "1": "aardbei", "2": "appel"}
#print(fruit)
print("Naar welke key zoek je? Key ")
x = input()
if x in fruit:
    print("Key komt voor in de dictionarie fruit.")
else:
    print("Key komt niet voor in dictionarie fruit")
    print(fruit)