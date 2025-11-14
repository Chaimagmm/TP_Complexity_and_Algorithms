import pandas as pd
import matplotlib.pyplot as plt

#  Charger les résultats
df = pd.read_csv("resultats_trie.csv")

#  Créer le graphique
plt.figure(figsize=(10, 6))
plt.plot(df["n"], df["temps_meilleur"], label="Meilleur cas", marker='o', markersize=3)
plt.plot(df["n"], df["temps_pire"], label="Pire cas", marker='x', markersize=3)

#  Personnalisation
plt.title("Temps d'exécution de la recherche séquentielle (tableau trié)", fontsize=13)
plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.legend()
plt.grid(True)

#  Enregistrer le graphique
plt.savefig("graph_trie.png", dpi=300)

