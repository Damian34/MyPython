import math

def circle(r):
    return math.pi*pow(r,2)

def triangle(a,h):
    return (a*h)/2

def rectangle(a,b=-1):
    if(b==-1):
        b=a
    return a*b

while 1:
    x = input("podaj nazwe figury i wartości: ")
    x2 = x.split(" ")
    field=-1;
    try:
        if(x2[0] == "koło"):
            field = circle(float(x2[1]))
        elif(x2[0]=="trójkąt"):
            field = triangle(float(x2[1]),float(x2[2]))
        elif(x2[0]=="trojkat"):
            if(len(x2) == 2):
                field = rectangle(float(x2[1]))
            else:
                field = rectangle(float(x2[1]),float(x2[2]))

        if(field != -1):
            print("Pole figury "+x2[0]+" o podanych wartościach wynosi "+str(field))
            break;
        else:
            print("wprowadziłeś nie poprawne dane spróbuj ponownie")

    except:
        print("wystąpił jakiś błąd spróbuj ponownie")




