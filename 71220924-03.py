#Input
p1 = int(input("P1:"))
p2 = int(input("P2:"))
p3 = int(input("P3:"))

#Proses
no_winner = (p1==p2==p3)
no_winner1 = (p1>21 and p2>21 and p3>21)
dekat_21 = p1!=21 or p2!=21 or p3!=21
x = 21-p1
y= 21-p2
z= 21-p3

if no_winner:
    print("Maka Tidak ada pemenang")
elif no_winner1:
    print("Maka Tidak ada pemenang")
elif p1 <= 21 and p1 > p2 and (p1 > p3 or p1 < p3):
    print("pemenangnya adalah P1")
elif p2 <= 21 and p2 > p1 and p2 > p3:
    print("Pemenangnya adalah P2")
elif p1 > 21 and p2 <= 21 and p2 > 21:
    print("Pemenangnya adalah P2")
elif p3 <=21 and p3 > p1 and p3> p2:
    print("Pemenangnya adalah P3")
elif p1 <=21 and abs (21-p2) and abs (21-p1) and abs (21-p3):
    print("Maka tidak ada pemenang")
elif dekat_21:
    if x==3 or x==2 or x==1:
        print("Maka pemenangnya adalah P1")
    elif y==3 or y==2 or y==1:
        print("Maka pemenangnya adalah P2 ")
    elif z==3 or z==2 or z==1:
        print("Maka pemenangnya adalah P3")
else:
    print("Input yang anda masukan salah!")
