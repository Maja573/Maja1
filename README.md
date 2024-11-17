import figury

print("Program rozpoczal dzialanie")
while True:
    inp = input()
    if inp == "stop":
        print("Program zakonczyl dzialanie")
        break
    elif inp == "a":
        a= float(input("a - "))
        b= float(input("b - "))
        c= float(input("c - "))
        print(f"obwód_kwadratu = {figury.obwod_kwadratu(a)}")
    
    elif inp == "b":
        a= float(input("a - "))
        b= float(input("b - "))
        print(f"obwód_prostokata = {figury.obwod_prostokata(a,b)}")
    
    elif inp == "b":
        a= float(input("a - "))
        h= float(input("h - "))
        print(f"obwód_rownolegloboku = {figury.obwod_rownolegloboku(a,h)}")
        
    elif inp == "c":
        a= float(input("a - "))
        b= float(input("b - "))
        c= float(input("c - "))
        d= float(input("d - "))
        print(f"obwód_trapezu = {figury.obwod_trapezu(a,b,c,d)}")
    
    elif inp == "d":
        a= float(input("a - "))
        b= float(input("b - "))
        c= float(input("c - "))
        print(f"obwód_trojkata = {figury.obwod_trojkata(a,b,c)}")
    
    elif inp == "e":
        a= float(input("a - "))
        print(f"obwód_trojkata_rownobocznego = {figury.obwod_trojkata_rownobocznego()}")
    
    elif inp == "f":
        r= float(input("r - "))
        print(f"obwód_kola = {figury.obwod_kola(r)}")
    
    elif inp == "g":
        a= float(input("a - "))
        print(f"obwód_rombu = {figury.obwod_rombu(a)}")
    
    elif inp == "h":
        a= float(input("a - "))
        print(f"pole_kwadratu = {figury.pole_kwadratu(a)}")
    
    elif inp == "i":
        a= float(input("a - "))
        b= float(input("b - "))
        print(f"pole_prostokata = {figury.pole_prostokata_(a,b)}")
   
    elif inp == "j":
        a= float(input("a - "))
        h= float(input("h - "))
        print(f"pole_rownolegloboku = {figury.pole_rownolegloboku(a,h)}")

    elif inp == "k":
        a= float(input("a - "))
        h= float(input("h - "))
        b= float(input("b - "))
        print(f"pole_trapezu = {figury.pole_trapezu(a,b,h)}")
    
    elif inp == "l":
        a= float(input("a - "))
        h= float(input("h - "))
        print(f"obwód_ = {figury.pole_trojkata(a,h)}")
       
    elif inp == "m":
        a= float(input("a - "))
        print(f"obwód_ = {figury.pole_trojkata_rownobocznego(a)}")
    
    elif inp == "n":
        r= float(input("r - "))
        print(f"obwód_ = {figury.pole_kola(r)}")
    
    elif inp == "o":
        d1= float(input("d1 - "))
        d2= float(input("d2 - "))
        print(f"obwód_ = {figury.pole_rombu(d1,d2)}")

import math

def obwod_kwadratu(a):
    return 4*a


def obwod_prostokata(a, b):
    return 2*(a + b)


def obwod_rownolegloboku(a, b):
    return 2*(a + b)


def obwod_trapezu(a, b, c, d):
    return a+b+c+d


def obwod_trojkata(a, b, c):
    return a+b+c


def obwod_trojkata_rownobocznego(a):
    return 3*a


def obwod_kola(r):
    return 2*math.pi*r


def obwod_rombu(a):
    return 4*a


def pole_kwadratu(a):
    return a**2


def pole_prostokata(a,b):
    return a*b


def pole_rownolegloboku(a,h):
    return a*h


def pole_trapezu(a,b,h):
    return 1/2*(a+b)*h


def pole_trojkata(a,h):
    return 1/2*a*h


def pole_trojkata_rownobocznego(a):
    return (math.sqrt(3)/4)*a**2


def pole_kola(r):
    return math.pi*r**2


def pole_rombu(d1,d2):
    return 1/2*d1*d2
