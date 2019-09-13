l = { }
y = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

def empty(x):
    v = len(x.keys())
    if(v is not 0):
        return False
    if(v is 0):
        return True
    
print(empty(l))
#print(l.key())
#print(y.key())