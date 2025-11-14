import random
import csv
import matplotlib.pyplot as plt

# --- MaxEtMinA avec compteur de comparaisons ---
def MaxEtMinA(tab):
    comparisons = 0
    max_val = tab[0]
    min_val = tab[0]
    for val in tab[1:]:
        comparisons += 1
        if val > max_val:
            max_val = val
        comparisons += 1
        if val < min_val:
            min_val = val
    return comparisons

# --- MaxEtMinB avec compteur de comparaisons ---
def MaxEtMinB(tab):
    n = len(tab)
    comparisons = 0

    # Initialisation
    if n % 2 == 0:
        comparisons += 1
        if tab[0] < tab[1]:
            min_val = tab[0]
            max_val = tab[1]
        else:
            min_val = tab[1]
            max_val = tab[0]
        start_idx = 2
    else:
        min_val = max_val = tab[0]
        start_idx = 1

    # Parcours par paires
    for i in range(start_idx, n-1, 2):
        a, b = tab[i], tab[i+1]
        comparisons += 1
        if a < b:
            comparisons += 2
            if a < min_val:
                min_val = a
            if b > max_val:
                max_val = b
        else:
            comparisons += 2
            if b < min_val:
                min_val = b
            if a > max_val:
                max_val = a
    return comparisons

# --- Lecture des tailles ---
with open("tailles.txt", "r") as f:
    tailles = [int(line.strip()) for line in f.readlines()]

# --- Fichier CSV pour sauvegarder les résultats ---
with open("comparaisons_maxmin.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "comparaisons_A", "comparaisons_B"])

    for n in tailles:
        tab = random.sample(range(n*10), n)  # nombres distincts
        comp_A = MaxEtMinA(tab)
        comp_B = MaxEtMinB(tab)
        writer.writerow([n, comp_A, comp_B])
        print(f"n={n}, comparaisons_A={comp_A}, comparaisons_B={comp_B}")

# --- Lecture des résultats pour tracé ---
df = []
with open("comparaisons_maxmin.csv", "r") as f:
    next(f)  # ignorer l'en-tête
    for line in f:
        n, cA, cB = map(float, line.strip().split(","))
        df.append((n, cA, cB))

n_vals = [x[0] for x in df]
comp_A = [x[1] for x in df]
comp_B = [x[2] for x in df]

# --- Graphique des comparaisons ---
plt.figure(figsize=(12,6))
plt.plot(n_vals, comp_A, marker='o', label="Comparaisons MaxEtMinA", color='skyblue')
plt.plot(n_vals, comp_B, marker='o', label="Comparaisons MaxEtMinB", color='orange')
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Nombre de comparaisons")
plt.title("Comparaison du nombre de comparaisons : MaxEtMinA vs MaxEtMinB")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graphe_maxmin_precis.png", dpi=300)
