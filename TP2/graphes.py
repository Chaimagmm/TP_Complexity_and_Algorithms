import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger le fichier results.csv
df = pd.read_csv("sizes.csv")

# Liste des algorithmes
algos = df['Algo'].unique()

# Largeur des barres
width = 0.35

for algo in algos:
    # Sélectionner les données pour l'algo courant
    data = df[df['Algo'] == algo]
    sizes = data['Size'].values
    best = data['BestCase'].values
    worst = data['PireCase'].values
    
    # Créer un histogramme côte à côte avec échelle LOG
    x = np.arange(len(sizes))
    plt.figure(figsize=(14, 7))
    
    plt.bar(x - width/2, best, width, label='Best Case', color='skyblue')
    plt.bar(x + width/2, worst, width, label='Worst Case', color='salmon')
    
    # ÉCHELLE LOGARITHMIQUE pour mieux voir les petites valeurs
    plt.yscale('log')
    
    # Ajouter labels et titres
    plt.xticks(x, sizes, rotation=45)
    plt.xlabel('Taille du tableau (N)')
    plt.ylabel('Temps d\'exécution (secondes) - Échelle log')
    plt.title(f'Histogramme du Meilleur et Pire Cas - {algo}')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7, which='both')
    plt.tight_layout()
    plt.savefig(f'histogram_{algo}.png', dpi=300)
    plt.show()

print("✓ Graphiques générés avec succès!")
