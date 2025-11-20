#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*===========================
    Structure pour retourner min, max et comparaisons
===========================*/
typedef struct {
    int min;
    int max;
    long long comparisons;
} MinMax;

/*===========================
    1. Approche Naïve (MaxEtMinA)
    Complexité théorique: 2(n-1) comparaisons
    
    IMPORTANT: Le nombre de comparaisons est 
    TOUJOURS 2(n-1), peu importe l'ordre des éléments!
===========================*/
MinMax MaxEtMinA(int tab[], int n, long long *comp) {
    MinMax result;
    *comp = 0;
    
    result.min = tab[0];
    result.max = tab[0];
    
    for (int i = 1; i < n; i++) {
        // Comparaison pour le minimum
        (*comp)++;
        if (tab[i] < result.min) {
            result.min = tab[i];
        }
        
        // Comparaison pour le maximum
        (*comp)++;
        if (tab[i] > result.max) {
            result.max = tab[i];
        }
    }
    
    result.comparisons = *comp;
    return result;
}

/*===========================
    2. Algorithme plus efficace (MaxEtMinB)
    Complexité théorique: 3n/2 - 2 comparaisons
    
    IMPORTANT: Le nombre de comparaisons est 
    TOUJOURS 3n/2 - 2, peu importe l'ordre des éléments!
===========================*/
MinMax MaxEtMinB(int tab[], int n, long long *comp) {
    MinMax result;
    *comp = 0;
    
    int debut = 0;
    
    // Initialisation selon parité de n
    if (n % 2 == 1) {
        // n impair : le premier élément devient min et max initial
        result.min = tab[0];
        result.max = tab[0];
        debut = 1;
    } else {
        // n pair : comparer les deux premiers éléments
        (*comp)++;
        if (tab[0] < tab[1]) {
            result.min = tab[0];
            result.max = tab[1];
        } else {
            result.min = tab[1];
            result.max = tab[0];
        }
        debut = 2;
    }
    
    // Traiter les éléments par paires
    for (int i = debut; i < n - 1; i += 2) {
        int petit, grand;
        
        // 1. Comparer les deux éléments de la paire
        (*comp)++;
        if (tab[i] < tab[i + 1]) {
            petit = tab[i];
            grand = tab[i + 1];
        } else {
            petit = tab[i + 1];
            grand = tab[i];
        }
        
        // 2. Comparer petit avec min actuel
        (*comp)++;
        if (petit < result.min) {
            result.min = petit;
        }
        
        // 3. Comparer grand avec max actuel
        (*comp)++;
        if (grand > result.max) {
            result.max = grand;
        }
    }
    
    result.comparisons = *comp;
    return result;
}

/*===========================
              MAIN
===========================*/
int main() {
    int sizes[] = {
        100000, 200000, 400000, 600000, 800000,
        1000000, 1200000, 1400000, 1600000, 1800000,
        2000000, 4000000, 5000000, 6000000, 7000000, 8000000
    };
    int count = sizeof(sizes) / sizeof(sizes[0]);
    
    // Fichier CSV pour les comparaisons
    FILE *csv = fopen("maxmin_comparaisons.csv", "w");
    if (!csv) {
        printf("Erreur ouverture CSV\n");
        return 1;
    }
    fprintf(csv, "Size,Algo,Comparaisons\n");
    
    srand(time(NULL));
    
    printf("\n╔════════════════════════════════════════════════════════════════════════╗\n");
    printf("║         ANALYSE DE COMPLEXITÉ : RECHERCHE MIN/MAX                     ║\n");
    printf("╚════════════════════════════════════════════════════════════════════════╝\n");
    printf("\nNOTE IMPORTANTE:\n");
    printf("Le nombre de comparaisons est CONSTANT pour chaque algorithme,\n");
    printf("peu importe si le tableau est trié ou non!\n");
    printf("- MaxEtMinA fait TOUJOURS 2(n-1) comparaisons\n");
    printf("- MaxEtMinB fait TOUJOURS 3n/2 - 2 comparaisons\n");
    
    for (int s = 0; s < count; s++) {
        int n = sizes[s];
        printf("\n┌─── Taille N = %d ───────────────────────────────────────────┐\n", n);
        
        int *tab = malloc(n * sizeof(int));
        long long compA, compB;
        
        /*===============================================
            Générer un tableau ALÉATOIRE (NON TRIÉ)
        ================================================*/
        for (int i = 0; i < n; i++) {
            tab[i] = rand() % (n * 10);
        }
        
        // Exécuter les deux algorithmes
        MinMax resultA = MaxEtMinA(tab, n, &compA);
        MinMax resultB = MaxEtMinB(tab, n, &compB);
        
        /*===============================================
            SAUVEGARDER LES RÉSULTATS
        ================================================*/
        fprintf(csv, "%d,MaxEtMinA,%lld\n", n, compA);
        fprintf(csv, "%d,MaxEtMinB,%lld\n", n, compB);
        
        /*===============================================
            AFFICHAGE
        ================================================*/
        printf("│\n");
        printf("│ Tableau aléatoire (non trié)\n");
        printf("│   Min trouvé: %d, Max trouvé: %d\n", resultA.min, resultA.max);
        printf("│\n");
        printf("│ MaxEtMinA (Naïve):\n");
        printf("│   Comparaisons : %lld\n", compA);
        printf("│   Théorique    : %d (2(n-1) = 2n-2)\n", 2*(n-1));
        printf("│   Match        : %s\n", (compA == 2*(n-1)) ? "✓ OUI" : "✗ NON");
        printf("│\n");
        printf("│ MaxEtMinB (Efficace):\n");
        printf("│   Comparaisons : %lld\n", compB);
        printf("│   Théorique    : %d (3n/2-2)\n", (3*n)/2 - 2);
        printf("│   Match        : %s\n", (compB == (3*n)/2 - 2) ? "✓ OUI" : "✗ NON");
        printf("│\n");
        printf("│ Gain de MaxEtMinB:\n");
        printf("│   Réduction    : %.2f%% de comparaisons\n", 
               100.0 * (compA - compB) / compA);
        printf("│   Ratio A/B    : %.2f\n", (double)compA / compB);
        printf("└────────────────────────────────────────────────────────────────┘\n");
        
        free(tab);
    }
    
    fclose(csv);
    
    printf("\n╔════════════════════════════════════════════════════════════════════════╗\n");
    printf("║ ✓ Fichier généré: maxmin_comparaisons.csv                             ║\n");
    printf("╚════════════════════════════════════════════════════════════════════════╝\n");
    
    printf("\n┌─── COMPLEXITÉ THÉORIQUE ──────────────────────────────────────┐\n");
    printf("│ MaxEtMinA: 2(n-1) = 2n - 2 comparaisons                       │\n");
    printf("│ MaxEtMinB: 3n/2 - 2 ≈ 1.5n - 2 comparaisons                   │\n");
    printf("│ Gain théorique: ~25%% de comparaisons en moins                │\n");
    printf("│                                                               │\n");
    printf("│ IMPORTANT: Ces valeurs sont CONSTANTES, peu importe          │\n");
    printf("│ l'ordre des éléments (trié, inversé, ou aléatoire)!          │\n");
    printf("└───────────────────────────────────────────────────────────────┘\n\n");
    
    return 0;
}
