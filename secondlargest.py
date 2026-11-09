list=[11,25,50,60,40]
largest=list[0]
Secondlargest=list[0]
for i in list:
    if i>largest:
        largest=i
for i in list:
    if i>Secondlargest and largest != i:
        Secondlargest=i

print("Largest=",Secondlargest)