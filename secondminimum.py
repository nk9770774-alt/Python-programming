list=[11,25,50,60,40]
Minimum=list[0]
SecondMinimum=float('inf')
for i in list:
    if i<Minimum:
        Minimum=i
for i in list:
    if i>Minimum and i < SecondMinimum:
        SecondMinimum=i
print("Minimum=",Minimum)
print("SecondMinimum=",SecondMinimum)