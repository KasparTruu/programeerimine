aasta = int(input("Sisesta aastaarv: "))
if (aasta % 400 == 0) or (aasta % 4 == 0 and aasta % 100 != 0):
    print(aasta, "on liigaasta.")
else:
    print(aasta, "on lihtaasta.")
