import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV généré par ton programme C
data = pd.read_csv('resultats_trie.csv')

# Créer une figure
plt.figure(figsize=(10, 6))

# Tracer le meilleur cas
plt.plot(data['n'], data['temps_meilleur'], label='Meilleur cas', color='green', linewidth=2)

# Tracer le pire cas
plt.plot(data['n'], data['temps_pire'], label='Pire cas', color='red', linewidth=2)

# Titres et labels
plt.title("Temps d'exécution de la recherche linéaire", fontsize=14)
plt.xlabel("Taille du tableau (n)", fontsize=12)
plt.ylabel("Temps (secondes)", fontsize=12)

# Afficher la légende
plt.legend()

# Afficher une grille
plt.grid(True)

# Axe des x en échelle logarithmique pour mieux visualiser les grandes tailles
plt.xscale('log')

# Afficher le graphe
#plt.show()

# Optionnel : sauvegarder le graphe dans un fichier image
plt.savefig("graphe_recherche_trie.png")
print("Graphe enregistré dans graphe_recherche_trie.png")

