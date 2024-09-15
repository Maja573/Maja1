
#Menu
print("Kalkulator")
print("#1 Pole powierzchni sześcianu")
print("#2 Pole powierzchni prostopadłościanu")
print("#3 Pole powierzchni graniastosłupa")
print("#4 Pole powierzchni ostrosłupa")
print("#5 objętość sześcianu")
print("#6 objętość prostopadłościanu")
print("#7 objętość graniastosłupa")
print("#8 objętość ostrosłupa")
print("#9 obwód kwadratu")
print("#10 obwód prostokąta")
print("#11 obwód równoległoboku")
print("#12 obwód trapezu")
print("#13 obwód trójkąta")
print("#14 obwód trójkąta równobocznego")
print("#15 pole kwadratu")
print("#16 pole prostokąta")
print("#17 pole równoległoboku")
print("#18 pole trapezu")
print("#19 pole trójkąta")
x = int(input("Podaj swój wybór: "))

if(x==1):
    a = float(input("Podaj bok sześcianu: "))
    print("Pole powierzchni sześcianu: ",(6*a*a))
elif(x==2):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    print("Pole powierzchni prostopadłościanu: ", (2*a*b+2*a*c+2*b*c))
elif(x==3):
    a = float(input("Podaj pole podstawy: "))
    b = float(input("Podaj pole boczne: "))
    print("Pole powierzchni graniastosłupa: ",(2*a+b))
elif(x==4):
    a = float(input("Podaj pole podstawy: "))
    b = float(input("Podaj pole boczne: "))
    print("Pole powierzchni ostrosłupa: ",(a+b))
elif(x==5):
    a = float(input("objętość sześcianu"))
    print("Objętość sześcianu: ",(a*a*a))
elif(x==6):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    print("objętość prostopadłościanu",(a*b*c))
elif(x==7):
    a = float(input("Podaj pole podstawy: "))
    b = float(input("Podj wysokość: "))
    print("objętość graniastosłupa: ",(a*b))
elif(x==8):
    a = float(input("Podaj pole podstawy: "))
    b = float(input("Podj wysokość: "))
    print("objętość ostrosłupa: ",(1/3*a*b))
elif(x==9):
    a = float(input("podaj bok a: "))
    print("obwód kwadratu ",(a+a+a+a))
elif(x==10):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    print("obwód prostokąta: ",(2*a+2*b))
elif(x==11):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    print("obwód równoległoboku: ",(2*a+2*b))
elif(x==12):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    d = float(input("Podaj bok d: "))
    print("obwód trapezu",(a+b+c+d))
elif(x==13):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    print("obwód trójkąta: ",(a+b+c))
elif(x==14):
    a = float(input("podaj bok a: "))
    print("obwód trójkąta równobocznego ",(a+a+a))
elif(x==15):
     a = float(input("podaj bok a: "))
     print("pole kwadratu: ",(a*a))
elif(x==16):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    print("pole prostokąta: ",(a+b))
elif(x==17):
     a = float(input("Podaj bok a: "))
     b = float(input("Podj wysokość: "))
     print("pole równoległoboku ",(a*b))
elif(x==18):
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    h = float(input("podaj wysokość: "))
    print("pole trapezu: ",((a+b)*c)/2)

















