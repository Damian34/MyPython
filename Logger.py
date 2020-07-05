
import time
from datetime import datetime

N=-1
while 1:
    x = input("podaj liczbe sekund: ")
    try:
        N=int(x)
    except:
        print("podana wartość nie jest liczbą, spróbuj ponownie")
    if N<0:
        print("liczba sekund nie może być ujemna lub równa 0 spróbuj ponownie")
    else:
        break;

f = open("time.txt", "w")

print("rozpoczynam zapis do pliku")
for nr in range(1,N+1):
    d1 = datetime.now()
    s=d1.strftime(str(nr)+" | %d %m %Y | %H:%M:%S | "+str(d1.timestamp())+"\n")
    f.write(s)
    time.sleep(1)
f.close()
print("zakończono zapis do pliku")



