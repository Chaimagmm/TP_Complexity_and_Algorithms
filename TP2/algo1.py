import time
import csv

# --- Fonction de recherche dichotomique ---
def rechElets_Dicho(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            return True
        elif tab[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False

# --- Fonction pour mesurer le temps moyen ---
def mesure_temps(func, *args, repetitions=1000):
    total = 0
    for _ in range(repetitions):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total += (end - start)
    return total / repetitions

# --- Fichiers ---
with open("tailles.txt", "r") as f_tailles, open("resultats_dicho_precis.csv", "w", newline='') as f_res:
    writer = csv.writer(f_res)
    writer.writerow(["n", "temps_meilleur", "temps_pire"])
    
    for ligne in f_tailles:
        n = int(ligne.strip())
        tab = [i * 2 for i in range(n)]  # tableau trié

        # Meilleur cas : élément du milieu
        x_meilleur = tab[len(tab) // 2]
        temps_meilleur = mesure_temps(rechElets_Dicho, tab, x_meilleur, repetitions=1000)

        # Pire cas : élément absent
        x_pire = -1
        temps_pire = mesure_temps(rechElets_Dicho, tab, x_pire, repetitions=1000)

        writer.writerow([n, temps_meilleur, temps_pire])

print("Mesures terminées. Résultats enregistrés dans resultats_dicho_precis.csv")

