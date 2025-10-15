import random

# Parametry normálního rozdělení
prumer = 170
smerodatna_odchylka = 10
pocet_studentu = 100

# Generování výšek studentů
vysky = [round(random.gauss(prumer, smerodatna_odchylka)) for _ in range(pocet_studentu)]
vysky = [min(max(vyska, 140), 210) for vyska in vysky]  # omezení na 150–200 cm

# Název výstupního souboru
nazev_souboru = "vysky_studentu.txt"

# Uložení do textového souboru
with open(nazev_souboru, "w", encoding="utf-8") as soubor:
    for i, vyska in enumerate(vysky, start=1):
        soubor.write(f"{vyska}\n")

print(f"Hotovo! Výšky studentů byly uloženy do souboru „{nazev_souboru}“.")
