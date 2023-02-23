#input
dadu_1 = int(input("Dadu 1:"))
dadu_2 = int(input("Dadu 2:"))
dadu_3 = int(input("Dadu 3:"))

#Proses 
royal = (dadu_1 + dadu_2 + dadu_3)
triple = (dadu_1== dadu_2==dadu_3)
flush = (dadu_1 == 4 and dadu_2 == 5 and dadu_3 == 6)
double = dadu_1== dadu_2 or dadu_1== dadu_3 or dadu_2==dadu_3
single = (dadu_1 != dadu_2) and (dadu_2!= dadu_3) and (dadu_3!=dadu_1)
lebih = (dadu_1>6) or (dadu_2>6) or (dadu_3>6)
if royal ==18:
    print("Royal")
elif lebih:
    print("Lebih dari 6")
elif triple:
    print("triple")
elif flush:
    print("Flush")
elif double:
    print("double")
elif single:
    print("Single")
