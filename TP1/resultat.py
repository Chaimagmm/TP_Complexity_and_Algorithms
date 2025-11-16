import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_csv('resultats.csv')

# Afficher les premières lignes pour vérification
print("Données chargées :")
print(df.head())
print(f"\nNombre total de nombres testés : {len(df)}")

# Vérifier quels nombres de chiffres sont présents dans les données
chiffres_presents = sorted(df['Chiffres'].unique())
print(f"Nombre de chiffres présents : {chiffres_presents}")

# Calculer la moyenne des temps d'exécution par nombre de chiffres et par algorithme
chiffres_group = df.groupby('Chiffres')[['Algo1', 'Algo2', 'Algo3', 'Algo4']].mean()

print("\nMoyennes par nombre de chiffres :")
print(chiffres_group)

# Créer l'histogramme
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Temps d\'exécution moyen des algorithmes de test de primalité', fontsize=16)

# Noms des algorithmes
algorithmes = ['Algo1 (n-1)', 'Algo2 (n/2)', 'Algo3 (sqrt(n))', 'Algo4 (optimisé)']
couleurs = ['skyblue', 'lightcoral', 'lightgreen', 'gold']

# Filtrer pour avoir seulement 3, 6, 9 et 12 chiffres (s'ils existent)
chiffres_cibles = [c for c in [3, 6, 9, 12] if c in df['Chiffres'].unique()]
print(f"Chiffres cibles disponibles : {chiffres_cibles}")

df_filtre = df[df['Chiffres'].isin(chiffres_cibles)]

# Graphique 1: Comparaison par algorithme (groupé par nombre de chiffres)
x = np.arange(len(chiffres_cibles))
largeur = 0.2

for i, algo in enumerate(['Algo1', 'Algo2', 'Algo3', 'Algo4']):
    moyennes = []
    for chiffres in chiffres_cibles:
        moy = df_filtre[df_filtre['Chiffres'] == chiffres][algo].mean()
        moyennes.append(moy)
    
    axes[0, 0].bar(x + i*largeur, moyennes, largeur, label=algorithmes[i], color=couleurs[i])

axes[0, 0].set_xlabel('Nombre de chiffres')
axes[0, 0].set_ylabel('Temps moyen (secondes)')
axes[0, 0].set_title('Comparaison des algorithmes par nombre de chiffres')
axes[0, 0].set_xticks(x + 1.5*largeur)
axes[0, 0].set_xticklabels(chiffres_cibles)
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Graphique 2: Temps par algorithme (empilé)
for i, chiffres in enumerate(chiffres_cibles):
    donnees_chiffres = []
    for algo in ['Algo1', 'Algo2', 'Algo3', 'Algo4']:
        moy = df_filtre[df_filtre['Chiffres'] == chiffres][algo].mean()
        donnees_chiffres.append(moy)
    
    axes[0, 1].bar(algorithmes, donnees_chiffres, label=f'{chiffres} chiffres', 
                   color=couleurs[i], bottom=None if i == 0 else None)

axes[0, 1].set_xlabel('Algorithmes')
axes[0, 1].set_ylabel('Temps moyen (secondes)')
axes[0, 1].set_title('Temps par algorithme (non empilé)')
axes[0, 1].legend()
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3)

# Graphique 3: Heatmap des performances (CORRIGÉ)
moyennes_algo_chiffres = df_filtre.groupby('Chiffres')[['Algo1', 'Algo2', 'Algo3', 'Algo4']].mean()
print(f"\nDimensions de la heatmap: {moyennes_algo_chiffres.shape}")

# Vérifier que nous avons des données pour la heatmap
if not moyennes_algo_chiffres.empty:
    im = axes[1, 0].imshow(moyennes_algo_chiffres.values, cmap='YlOrRd', aspect='auto')

    axes[1, 0].set_xticks(range(len(algorithmes)))
    axes[1, 0].set_xticklabels([a.split(' ')[0] for a in algorithmes])
    axes[1, 0].set_yticks(range(len(chiffres_cibles)))
    axes[1, 0].set_yticklabels([f'{c} chiffres' for c in chiffres_cibles])
    axes[1, 0].set_title('Heatmap des temps d\'exécution')

    # Ajouter les valeurs dans la heatmap (CORRIGÉ - utilisation des bonnes dimensions)
    for i in range(len(moyennes_algo_chiffres)):  # i pour les lignes (chiffres)
        for j in range(len(moyennes_algo_chiffres.columns)):  # j pour les colonnes (algorithmes)
            text = axes[1, 0].text(j, i, f'{moyennes_algo_chiffres.values[i, j]:.6f}',
                                  ha="center", va="center", color="black", fontsize=8)
else:
    axes[1, 0].text(0.5, 0.5, 'Pas de données disponibles', 
                   ha='center', va='center', transform=axes[1, 0].transAxes)
    axes[1, 0].set_title('Heatmap - Pas de données')

# Graphique 4: Ratio de performance (Algo1 comme référence)
if len(chiffres_cibles) > 0:
    algo1_moyennes = df_filtre.groupby('Chiffres')['Algo1'].mean()
    ratios = {}
    for algo in ['Algo2', 'Algo3', 'Algo4']:
        algo_moyennes = df_filtre.groupby('Chiffres')[algo].mean()
        ratios[algo] = algo1_moyennes / algo_moyennes

    for i, (algo, ratio) in enumerate(ratios.items()):
        axes[1, 1].plot(chiffres_cibles, ratio.values, marker='o', 
                       label=algorithmes[i+1], color=couleurs[i+1])

    axes[1, 1].axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Référence Algo1')
    axes[1, 1].set_xlabel('Nombre de chiffres')
    axes[1, 1].set_ylabel('Ratio de performance (vs Algo1)')
    axes[1, 1].set_title('Amélioration de performance relative')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
else:
    axes[1, 1].text(0.5, 0.5, 'Pas de données disponibles', 
                   ha='center', va='center', transform=axes[1, 1].transAxes)
    axes[1, 1].set_title('Ratio de performance - Pas de données')

plt.tight_layout()
plt.savefig('comparaison_algorithmes.png', dpi=300, bbox_inches='tight')


# Statistiques détaillées
print("\n" + "="*50)
print("STATISTIQUES DÉTAILLÉES")
print("="*50)

for chiffres in chiffres_cibles:
    print(f"\n--- {chiffres} chiffres ---")
    donnees_chiffres = df_filtre[df_filtre['Chiffres'] == chiffres]
    for i, algo in enumerate(['Algo1', 'Algo2', 'Algo3', 'Algo4']):
        moy = donnees_chiffres[algo].mean()
        std = donnees_chiffres[algo].std()
        print(f"{algorithmes[i]}: {moy:.6f} ± {std:.6f} sec")

# Sauvegarder les statistiques
if not df_filtre.empty:
    stats_df = df_filtre.groupby('Chiffres')[['Algo1', 'Algo2', 'Algo3', 'Algo4']].agg(['mean', 'std'])
    stats_df.to_csv('statistiques_detaillees.csv')
    print("\nStatistiques détaillées sauvegardées dans 'statistiques_detaillees.csv'")
else:
    print("\nAucune donnée à sauvegarder")
