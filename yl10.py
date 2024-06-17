nimi = input("Sisesta oma nimi: ")
print(f"Tere, {nimi}!")

elukoht = input("Sisesta oma elukoht: ")
if elukoht.lower() == "saaremaa":
    print("Tere, saarlane!")

vanus = int(input("Sisesta oma vanus: "))
if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Palju õnne, sa oled täisealine!")
else:
    print("Sa võid autot juhtida.")