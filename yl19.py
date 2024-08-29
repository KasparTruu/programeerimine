tekst = "Kirjuta tekst: "

taishaalikud_arv = 0
for taht in tekst:
    if taht.lower() in "aeiouõäöü":
        taishaalikud_arv += 1

print("Täishäälikute arv tekstis on: ", taishaalikud_arv)
#taht.lower teeb tähed väiketäheks 