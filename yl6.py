arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
arv3 = float(input("Sisesta kolmas arv: "))

if arv2 > max_arv:
    max_arv = arv2


if arv3 > max_arv:
    max_arv = arv3

print("Maksimum arv on:", max_arv)
