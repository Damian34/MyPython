
tab=[]

while 1:
    x = input("podaj nazwe produktu: ")
    if(x=="exit"):
        break
    else:
        tab.append(x)
tab2={}
for p in tab:
    while 1:
        x = input("podaj cene produktu "+p+": ")
        try:
            x2=float(x)
            tab2.update({p.isupper(): x2})
            break
        except:
            print("wprowadzona wartoś nie jest liczbą")

sum = 0
for i in tab2.values():
    sum +=i
print("łączny koszt produktów to: "+str(sum),end="")
if(sum <= 100):
    print(", więc jesteś w stanie to zakupić za 100zł")
else:
    print(", więc nie kupisz tego mając tylko 100zł")

