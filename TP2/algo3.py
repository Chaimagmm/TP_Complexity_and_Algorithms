import time

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


# --- Fichiers ---
f_tailles = open("tailles.txt", "r")
f_res = open("resultats_dicho.csv", "w")

# En-tête du CSV
f_res.write("n,temps_meilleur,temps_pire\n")

# --- Mesure des temps ---
for ligne in f_tailles:
    n = int(ligne.strip())
    tab = [i * 2 for i in range(n)]  # tableau trié

    # --- Meilleur cas : élément du milieu ---
    x_meilleur = tab[len(tab) // 2]
    start = time.perf_counter()
    rechElets_Dicho(tab, x_meilleur)
    end = time.perf_counter()
    temps_meilleur = end - start

    # --- Pire cas : élément absent ---
    x_pire = -1  # n’existe pas dans le tableau
    start = time.perf_counter()
    rechElets_Dicho(tab, x_pire)
    end = time.perf_counter()
    temps_pire = end - start

    # --- Sauvegarde des résultats ---
    f_res.write(f"{n},{temps_meilleur},{temps_pire}\n")

f_tailles.close()
f_res.close()
print("Mesures terminées. Résultats enregistrés dans resultats_dicho.csv")

