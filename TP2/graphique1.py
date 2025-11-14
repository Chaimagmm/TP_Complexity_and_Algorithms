import pandas as pd
import matplotlib.pyplot as plt

#  Chargement du fichier CSV généré précédemment
df = pd.read_csv("resultats_non_trie.csv")

#  Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(df["n"], df["temps_meilleur"], label="Meilleur cas", marker='o', markersize=3)
plt.plot(df["n"], df["temps_pire"], label="Pire cas", marker='x', markersize=3)

#  Personnalisation
plt.title("Temps d'exécution de la recherche séquentielle (tableau non trié)", fontsize=13)
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.legend()
plt.grid(True)

#  Enregistrer le graphe
plt.savefig("graph_non_trie.png", dpi=300)

