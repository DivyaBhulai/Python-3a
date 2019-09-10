def priemgetal(x):
    for i in range(2, int(x/2)):
        if(x % i == 0):
            print("het getal is geen priemgetal")
            return
        else:
            print("het getal is een priemgetal")
            return

                
priemgetal(23)