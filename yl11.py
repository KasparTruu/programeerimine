sisend = input("Sisendina string: ").strip()
if len(sisend) < 7 or len(sisend) % 2 != 0:
    print("Sisend peab olema vähemalt 7 sümbolit pikk ja sümbolite arv peab olema paarituarvuline.")
else:
    keskmine_indeks = len(sisend) // 2
    keskmised_sümbolid = sisend[keskmine_indeks-1:keskmine_indeks+2]
    print("Kolm keskmist sümbolit:", keskmised_sümbolid)
    #(.strip()): Eemaldab kõik tühikud stringi algusest ja lõpust.
    #len(sisend) < 7 )Kontrollib, kas stringi pikkus on väiksem kui 7 sümbolit.
    #len(sisend) // 2: Leiab stringi keskmise indeksi, kasutades täisarvude jagamist.