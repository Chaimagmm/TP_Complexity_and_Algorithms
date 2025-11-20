import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger le fichier CSV
df = pd.read_csv("maxmin_comparaisons.csv")

print("\n" + "="*80)
print("VISUALISATION DE LA COMPLEXITÉ EN NOMBRE DE COMPARAISONS")
print("="*80 + "\n")

# Extraire les données
data_A = df[df['Algo'] == 'MaxEtMinA']
data_B = df[df['Algo'] == 'MaxEtMinB']

sizes = data_A['Size'].values
comp_A = data_A['Comparaisons'].values
comp_B = data_B['Comparaisons'].values

# ====================================
# GRAPHIQUE 1 : MaxEtMinA (Naïve)
# ====================================
plt.figure(figsize=(14, 7))

x = np.arange(len(sizes))
bars = plt.bar(x, comp_A, color='coral', alpha=0.85, edgecolor='darkred', linewidth=1.5)

# Ajouter la courbe théorique
theory_A = 2 * (sizes - 1)
plt.plot(x, theory_A, 'r--', linewidth=2.5, marker='o', markersize=6, 
         label='Courbe théorique: 2(n-1)', alpha=0.7)

# Ajouter les valeurs sur quelques barres
indices_a_afficher = [0, len(sizes)//2, -1]
for idx in indices_a_afficher:
    bar = bars[idx]
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height * 1.01,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.xlabel('Taille du tableau (N)', fontsize=13)
plt.ylabel('Nombre de comparaisons', fontsize=13)
plt.title('MaxEtMinA (Approche Naïve)\nComplexité: 2(n-1) comparaisons', 
          fontsize=15, fontweight='bold', pad=15)
plt.xticks(x, [f'{size:,}' for size in sizes], rotation=45, ha='right')
plt.legend(fontsize=11, loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('graph1_MaxEtMinA.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Graphique 1 généré : graph1_MaxEtMinA.png")

# ====================================
# GRAPHIQUE 2 : MaxEtMinB (Efficace)
# ====================================
plt.figure(figsize=(14, 7))

bars = plt.bar(x, comp_B, color='skyblue', alpha=0.85, edgecolor='darkblue', linewidth=1.5)

# Ajouter la courbe théorique
theory_B = 1.5 * sizes - 2
plt.plot(x, theory_B, 'b--', linewidth=2.5, marker='s', markersize=6, 
         label='Courbe théorique: 3n/2 - 2', alpha=0.7)

# Ajouter les valeurs sur quelques barres
for idx in indices_a_afficher:
    bar = bars[idx]
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height * 1.01,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.xlabel('Taille du tableau (N)', fontsize=13)
plt.ylabel('Nombre de comparaisons', fontsize=13)
plt.title('MaxEtMinB (Approche Efficace)\nComplexité: 3n/2 - 2 comparaisons', 
          fontsize=15, fontweight='bold', pad=15)
plt.xticks(x, [f'{size:,}' for size in sizes], rotation=45, ha='right')
plt.legend(fontsize=11, loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('graph2_MaxEtMinB.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Graphique 2 généré : graph2_MaxEtMinB.png")

# ====================================
# GRAPHIQUE 3 : Comparaison des deux algorithmes
# ====================================
plt.figure(figsize=(16, 7))

width = 0.35
bars1 = plt.bar(x - width/2, comp_A, width, label='MaxEtMinA (Naïve)', 
                color='coral', alpha=0.85, edgecolor='darkred', linewidth=1.5)
bars2 = plt.bar(x + width/2, comp_B, width, label='MaxEtMinB (Efficace)', 
                color='dodgerblue', alpha=0.85, edgecolor='darkblue', linewidth=1.5)

# Ajouter les courbes théoriques
plt.plot(x - width/2, theory_A, 'r--', linewidth=2, alpha=0.5, label='Théorique A: 2(n-1)')
plt.plot(x + width/2, theory_B, 'b--', linewidth=2, alpha=0.5, label='Théorique B: 3n/2-2')

# Ajouter les valeurs et le pourcentage de gain
indices_comparaison = [0, 5, 10, -1]
for idx in indices_comparaison:
    # MaxEtMinA
    bar = bars1[idx]
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=8)
    
    # MaxEtMinB
    bar = bars2[idx]
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=8)
    
    # Pourcentage de gain
    gain = 100 * (comp_A[idx] - comp_B[idx]) / comp_A[idx]
    plt.text(x[idx], max(comp_A[idx], comp_B[idx]) * 1.08,
            f'-{gain:.1f}%',
            ha='center', va='bottom', fontsize=10, 
            fontweight='bold', color='green',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

plt.xlabel('Taille du tableau (N)', fontsize=13)
plt.ylabel('Nombre de comparaisons', fontsize=13)
plt.title('Comparaison : MaxEtMinA vs MaxEtMinB\nGain: ~25% de comparaisons en moins (Tableau aléatoire)', 
          fontsize=15, fontweight='bold', pad=15)
plt.xticks(x, [f'{size:,}' for size in sizes], rotation=45, ha='right')
plt.legend(fontsize=11, loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('graph3_Comparaison.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Graphique 3 généré : graph3_Comparaison.png")

# ====================================
# TABLEAU RÉCAPITULATIF
# ====================================
print("\n" + "="*85)
print("TABLEAU RÉCAPITULATIF (Tableaux aléatoires non triés)")
print("="*85)
print(f"{'Taille N':<13} {'MaxEtMinA':<14} {'MaxEtMinB':<14} {'Réduction':<14} {'Ratio A/B':<12}")
print("-"*85)

# Afficher quelques lignes représentatives
indices_tableau = [0, 5, 10, -1]
for idx in indices_tableau:
    size = sizes[idx]
    a_comp = comp_A[idx]
    b_comp = comp_B[idx]
    reduction = 100 * (a_comp - b_comp) / a_comp
    ratio = a_comp / b_comp
    
    print(f"{size:<13,} {int(a_comp):<14,} {int(b_comp):<14,} {reduction:<13.2f}% {ratio:<12.3f}")

print("-"*85)

# Vérification avec la théorie
print("\nVÉRIFICATION AVEC LA THÉORIE:")
print("-"*85)
for idx in [0, -1]:
    size = sizes[idx]
    a_comp = comp_A[idx]
    b_comp = comp_B[idx]
    a_theory = 2 * (size - 1)
    b_theory = int(1.5 * size - 2)
    
    print(f"\nN = {size:,}")
    print(f"  MaxEtMinA: {int(a_comp):,} comparaisons (théorique: {a_theory:,}) → Match: {'✓' if a_comp == a_theory else '✗'}")
    print(f"  MaxEtMinB: {int(b_comp):,} comparaisons (théorique: {b_theory:,}) → Match: {'✓' if b_comp == b_theory else '✗'}")

print("\n" + "="*85)
print("COMPLEXITÉ THÉORIQUE:")
print("  • MaxEtMinA: 2(n-1) comparaisons - CONSTANT peu importe l'ordre!")
print("  • MaxEtMinB: 3n/2 - 2 comparaisons - CONSTANT peu importe l'ordre!")
print("  • Gain: ~25% de comparaisons en moins avec MaxEtMinB")
print("="*85)

print("\n✓ Tous les graphiques ont été générés avec succès!")
print("  - graph1_MaxEtMinA.png      (Histogramme pour Algo 1)")
print("  - graph2_MaxEtMinB.png      (Histogramme pour Algo 2)")
print("  - graph3_Comparaison.png    (Comparaison des deux algorithmes)")
print()
