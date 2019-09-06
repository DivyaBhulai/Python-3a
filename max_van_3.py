def getallen():    
    x = int(input("getal x = "))
    y = int(input("getal y = "))
    z = int(input("getal z = "))
    if(x > y and x > z):
        print("het hoogste getal is x")
    if(y > x and y > z):
        print("het hoogste getal is y")
    if(z > x and z > y):
        print("het hoogste getal is z")
    if(x == z or x == y or y == z):
        print("Er zijn 2 even hoge getallen")
    
getallen()

