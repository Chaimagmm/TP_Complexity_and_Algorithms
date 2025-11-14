import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Charger les résultats ---
df = pd.read_csv("resultats_maxmin.csv")

# --- Échantillonner pour lisibilité si trop de points ---
echantillon = df.iloc[::max(1, len(df)//20)]  # environ 20 points

n = echantillon["n"]
temps = echantillon["temps_moyen"]

# --- Tracé ---
plt.figure(figsize=(12, 6))
plt.plot(n, temps, marker='o', linestyle='-', color='skyblue', label="Temps moyen MaxEtMinA")

plt.xlabel("Taille du tableau (n)")
plt.ylabel("Temps moyen d'exécution (secondes)")
plt.title("Recherche du maximum et minimum : Approche naïve")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("graphe_maxmin.png", dpi=300)

