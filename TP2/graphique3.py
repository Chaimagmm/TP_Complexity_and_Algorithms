import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 📂 Charger les résultats CSV
df = pd.read_csv("resultats_dicho_precis.csv")

# Pour garder un histogramme lisible, on prend un échantillon si nécessaire
echantillon = df.iloc[::len(df)//20]  # 20 barres maximum pour la lisibilité

n = echantillon["n"]
temps_meilleur = echantillon["temps_meilleur"]
temps_pire = echantillon["temps_pire"]

x = np.arange(len(n))  # positions des barres sur l'axe x
width = 0.35  # largeur des barres

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, temps_meilleur, width, label="Meilleur cas", color='skyblue')
plt.bar(x + width/2, temps_pire, width, label="Pire cas", color='salmon')

plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Recherche dichotomique - Meilleur et pire cas")
plt.xticks(x, n, rotation=45)
plt.legend()
plt.grid(axis='y')

plt.tight_layout()
plt.savefig("histogramme_dichoto.png", dpi=300)


