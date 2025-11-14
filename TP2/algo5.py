import time
import random
import csv
import matplotlib.pyplot as plt

# --- Fonction MaxEtMinA ---
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
    return min_val, max_val, comparisons

# --- Fonction MaxEtMinB ---
def MaxEtMinB(tab):
    n = len(tab)
    comparisons = 0

    # Initialisation
    if n % 2 == 0:
        if tab[0] < tab[1]:
            min_val = tab[0]
            max_val = tab[1]
        else:
            min_val = tab[1]
            max_val = tab[0]
        comparisons += 1
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
    return min_val, max_val, comparisons

# --- Mesure du temps moyen et comparaisons ---
def mesure_algo(func, tab, repetitions=50):
    total_time = 0
    total_comp = 0
    for _ in range(repetitions):
        start = time.perf_counter()
        _, _, comp = func(tab)
        end = time.perf_counter()
        total_time += (end - start)
        total_comp += comp
    return total_time / repetitions, total_comp / repetitions

# --- Lecture des tailles ---
with open("tailles.txt", "r") as f:
    tailles = [int(line.strip()) for line in f.readlines()]

# --- CSV des résultats ---
with open("resultats_maxmin_comparaison.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "temps_A", "comp_A", "temps_B", "comp_B"])

    for n in tailles:
        tab = random.sample(range(n*10), n)  # nombres distincts
        temps_A, comp_A = mesure_algo(MaxEtMinA, tab)
        temps_B, comp_B = mesure_algo(MaxEtMinB, tab)
        writer.writerow([n, temps_A, comp_A, temps_B, comp_B])
        print(f"n={n}, temps_A={temps_A:.6f}, comp_A={comp_A}, temps_B={temps_B:.6f}, comp_B={comp_B}")

# --- Visualisation graphique ---
df = []
with open("resultats_maxmin_comparaison.csv", "r") as f:
    next(f)  # ignorer l'en-tête
    for line in f:
        n, tA, cA, tB, cB = map(float, line.strip().split(","))
        df.append((n, tA, cA, tB, cB))

n_vals = [x[0] for x in df]
temps_A = [x[1] for x in df]
comp_A = [x[2] for x in df]
temps_B = [x[3] for x in df]
comp_B = [x[4] for x in df]

plt.figure(figsize=(12,6))
plt.plot(n_vals, temps_A, marker='o', label="Temps MaxEtMinA", color='skyblue')
plt.plot(n_vals, temps_B, marker='o', label="Temps MaxEtMinB", color='orange')
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps moyen d'exécution (s)")
plt.title("Comparaison des temps d'exécution : MaxEtMinA vs MaxEtMinB")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
plt.plot(n_vals, comp_A, marker='o', label="Comparaisons MaxEtMinA", color='skyblue')
plt.plot(n_vals, comp_B, marker='o', label="Comparaisons MaxEtMinB", color='orange')
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Nombre moyen de comparaisons")
plt.title("Comparaison du nombre de comparaisons : MaxEtMinA vs MaxEtMinB")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graphe_maxmin_precis.png", dpi=300)
