
import random
import math

def percent(x):
    p= math.floor(x*100)
    return str(p)+"%"

tab=[]
for i in range(10):
    tab.append(round(random.random(),5))

f = open("percent.txt", "w")

for i in sorted(tab):
    f.write((str(i)+" ; "+percent(i)))

    if(sorted(tab)[-1]!= i):
        f.write("\n")
f.close()



