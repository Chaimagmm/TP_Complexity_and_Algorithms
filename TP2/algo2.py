import time
import csv

#  Fonction de recherche séquentielle optimisée pour tableau trié
def rechElets_TabTries(tab, x):
    for val in tab:
        if val == x:
            return True
        elif val > x:
            return False  # inutile de continuer
    return False


#  Lecture des tailles + enregistrement des résultats
with open("tailles.txt", "r") as f_tailles, open("resultats_trie.csv", "w", newline="") as f_res:
    writer = csv.writer(f_res)
    writer.writerow(["n", "temps_meilleur", "temps_pire"])

    for line in f_tailles:
        n = int(line.strip())

        #  Génération d’un tableau trié croissant
        tab = [i * 2 for i in range(n)]

        #  Meilleur cas (élément au début)
        x_meilleur = tab[0]
        start = time.perf_counter()
        rechElets_TabTries(tab, x_meilleur)
        end = time.perf_counter()
        temps_meilleur = end - start

        #  Pire cas (élément absent)
        x_pire = tab[-1] + 1
        start = time.perf_counter()
        rechElets_TabTries(tab, x_pire)
        end = time.perf_counter()
        temps_pire = end - start

        #  Sauvegarde dans le CSV
        writer.writerow([n, temps_meilleur, temps_pire])

print("✅ Mesures terminées. Résultats enregistrés dans 'resultats_trie.csv'")

