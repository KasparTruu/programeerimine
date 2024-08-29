import random

valikud = ["kivi", "paber", "käärid"]

while True:
    arvuti_valik = random.choice(valikud)
    kasutaja_valik = input("Vali kivi, paber või käärid (või 'lõpeta' lõpetamiseks): ").lower()

    if kasutaja_valik == "lõpeta":
        print("Mäng lõppenud. Aitäh mängimast!")
        break

    if kasutaja_valik not in valikud:
        print("Vale valik! Palun vali 'kivi', 'paber' või 'käärid'.")
        continue

    print(f"Arvuti valis: {arvuti_valik}")

    if kasutaja_valik == arvuti_valik:
        print("Viik!")
    elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik == "paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik == "käärid" and arvuti_valik == "paber"):
        print("Sina võitsid!")
    else:
        print("Arvuti võitis!")

    print()
