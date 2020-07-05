
tab=[]

while 1:
    x = input("podaj liczbe: ")
    if(x=="exit"):
        print("podałeś "+str(len(tab))+" licz, to one:")
        for nr in tab:
            print(str(nr))
        break
    else:
        try:
            x2=float(x)
            tab.append(x)
        except:
            print("Podałeś "+str(len(tab))+" liczb. Dalej się nie bawię")

