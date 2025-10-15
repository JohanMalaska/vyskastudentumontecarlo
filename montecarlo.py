import random
import matplotlib.pyplot as plt

# 1. Načtení výšek ze souboru
nazev_souboru = "vysky_studentu.txt"

vysky = []

with open(nazev_souboru, "r", encoding="utf-8") as soubor:
    for radek in soubor:
        try:
            vyska = int(radek.strip())
            vysky.append(vyska)
        except ValueError:
            pass  # přeskočí neplatné řádky

# Kontrola, že máme data
if not vysky:
    print("Soubor neobsahuje žádné platné výšky.")
    exit()


pod_150 = sum(1 for v in vysky if v < 150)
nad_200 = sum(1 for v in vysky if v > 200)

print("Statistika extrémních výšek:")
print(f"👶 Počet studentů pod 150 cm: {pod_150}")
print(f"🧔 Počet studentů nad 200 cm: {nad_200}")
print()
# 2. Monte Carlo simulace
pocet_simulaci = 1000
velikost_vzorku = 30

prumery = []

for _ in range(pocet_simulaci):
    vzorek = random.choices(vysky, k=velikost_vzorku)
    prumer = sum(vzorek) / velikost_vzorku
    prumery.append(prumer)

# 3. Vykreslení histogramu a uložení do souboru
plt.figure(figsize=(10, 6))
plt.hist(prumery, bins=30, color='lightgreen', edgecolor='black')
plt.title(f"Monte Carlo simulace průměrné výšky ({pocet_simulaci} běhů)")
plt.xlabel("Průměrná výška (cm)")
plt.ylabel("Počet výskytů")
plt.grid(True)
plt.tight_layout()

# Uložení grafu do souboru
nazev_obrazku = "graf_monte_carlo_vysky.png"
plt.savefig(nazev_obrazku, dpi=300)
print(f"Graf byl uložen jako '{nazev_obrazku}'.")

# Nepotřebujeme plt.show(), pokud graf jen ukládáme
# plt.show()  # odkomentuj, pokud chceš graf i zobrazit
