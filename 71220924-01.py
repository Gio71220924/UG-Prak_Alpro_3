#Input
jarak = int(input("Jarak:"))
batas_a = int(input("Batas:"))
Nilai = int(input("Nilai:"))

# Proses
batas_a_min = batas_a-jarak
batas_b_plus = batas_a_min - jarak
batas_b = batas_b_plus - jarak
batas_b_min = batas_b - jarak
batas_c_plus = batas_b_min - jarak
batas_c = batas_c_plus - jarak
batas_d = batas_c - jarak
batas_e = batas_d - jarak

if Nilai >= batas_a:
    print("A")
elif Nilai >= batas_a_min:
    print("A-")
elif Nilai >= batas_b_plus:
    print("B+")
elif Nilai >= batas_b:
    print("B")
elif Nilai >= batas_b_min:
    print("B-")
elif Nilai >= batas_c_plus:
    print("C+")
elif Nilai >= batas_c:
    print("C")
elif Nilai >= batas_d:
    print("D")
else:
    print("E")