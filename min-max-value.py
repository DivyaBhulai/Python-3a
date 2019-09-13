getallen = {1: 10, 2: 20, 3: 30, 4: 40}

def cijfers(g):
    x = min(g)
    y = max(g)
    z = g.get(x)
    a = g.get(y)
    return z, a
    
    
print(cijfers(getallen))
