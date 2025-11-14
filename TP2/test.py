import time
import random
import csv

# 🔎 Fonction de recherche séquentielle dans un tableau non trié
def rechElets_TabNonTries(tab, x):
    for val in tab:
        if val == x:
            return True  # trouvé
    return False  # non trouvé


# 📂 Fichiers d’entrée et de sortie
with open("tailles.txt", "r") as f_tailles, open("resultats_non_trie.csv", "w", newline="") as f_res:
    writer = csv.writer(f_res)
    writer.writerow(["n", "temps_meilleur", "temps_pire"])

    # 🔁 Lecture de chaque taille dans le fichier
    for line in f_tailles:
        n = int(line.strip())

        # 🧩 Génération d’un tableau aléatoire de taille n
        tab = [random.randint(0, n * 10) for _ in range(n)]

        # ⏱️ Mesure du temps pour le meilleur cas (élément au début)
        x_meilleur = tab[0]
        start = time.perf_counter()
        rechElets_TabNonTries(tab, x_meilleur)
        end = time.perf_counter()
        temps_meilleur = end - start

        # ⏱️ Mesure du temps pour le pire cas (élément absent)
        x_pire = -1  # valeur impossible
        start = time.perf_counter()
        rechElets_TabNonTries(tab, x_pire)
        end = time.perf_counter()
        temps_pire = end - start

        # 💾 Sauvegarde des résultats dans le CSV
        writer.writerow([n, temps_meilleur, temps_pire])

print("✅ Mesures terminées. Résultats enregistrés dans 'resultats_non_trie.csv'")

