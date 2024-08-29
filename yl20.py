
x = int(input("Sisesta arv, mille kohta soovid korrutustabelit: "))

for i in range(13):
    print(f"{x} x {i} = {x * i}")
    # for tsükkel itererib vahemikus 0 kuni 12.