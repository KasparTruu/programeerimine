import random

# Arvuti mõtleb välja arvu nullist sajani
arv = random.randint(0, 100)

while True:
    # Kasutaja pakkumine
    pakkumine = int(input("Paku arvu: "))

    # Vihje, kas pakkumine on õigest arvust suurem või väiksem
    if pakkumine > arv:
        print("Pakkumine on suurem!")
    elif pakkumine < arv:
        print("Pakkumine on väiksem!")
    else:
        print("Õige arv! Arvuti mõtles välja arvu", arv)
        break