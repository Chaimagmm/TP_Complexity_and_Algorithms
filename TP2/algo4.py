import time
import random
import csv

# --- Fonction MaxEtMinA ---
def MaxEtMinA(tab):
    max_val = tab[0]
    min_val = tab[0]
    for val in tab[1:]:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    return max_val, min_val

# --- Mesure du temps moyen ---
def mesure_temps(func, tab, repetitions=100):
    total = 0
    for _ in range(repetitions):
        start = time.perf_counter()
        func(tab)
        end = time.perf_counter()
        total += (end - start)
    return total / repetitions

# --- Lecture des tailles ---
with open("tailles.txt", "r") as f:
    tailles = [int(line.strip()) for line in f.readlines()]

# --- CSV de résultats ---
with open("resultats_maxmin.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "temps_moyen"])  # entêtes

    for n in tailles:
        tab = [random.randint(0, n*10) for _ in range(n)]
        temps = mesure_temps(MaxEtMinA, tab, repetitions=100)
        writer.writerow([n, temps])
        print(f"n={n}, temps moyen={temps:.8f} s")

