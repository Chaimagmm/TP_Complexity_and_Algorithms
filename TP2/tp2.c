#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*===========================
    1 - Recherche Non Tries
===========================*/
int rechElets_TabNonTries(int tab[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return 1;
    }
    return 0;
}

/*===========================
    2 - Recherche Triee
===========================*/
int rechElets_TabTries(int tab[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return 1;
        if (tab[i] > x)
            return 0;
    }
    return 0;
}

/*===========================
    3 - Recherche Dichotomique
===========================*/
int rechElets_Dicho(int tab[], int n, int x) {
    int debut = 0, fin = n - 1, milieu;
    while (debut <= fin) {
        milieu = (debut + fin) / 2;
        if (tab[milieu] == x)
            return 1;
        if (tab[milieu] < x)
            debut = milieu + 1;
        else
            fin = milieu - 1;
    }
    return 0;
}

/*===========================
    Temps d'exécution CORRIGÉ
===========================*/
double measure(int (*func)(int[], int, int), int tab[], int n, int x, int innerReps) {
    volatile int result;  // volatile empêche l'optimisation
    clock_t d = clock();
    
    for (int i = 0; i < innerReps; i++) {
        result = func(tab, n, x);  // Stocker le résultat
    }
    
    clock_t f = clock();
    
    // Utiliser result pour éviter l'optimisation complète
    if (result < -1000) printf("%d", result);
    
    return (double)(f - d) / CLOCKS_PER_SEC / innerReps;
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
    
    // AJUSTEMENT : Plus de répétitions pour les petites tailles
    int outerReps = 50;
    int innerReps = 1000;  // Augmenté pour avoir des temps mesurables
    
    FILE *csv = fopen("sizes.csv", "w");
    if (!csv) {
        printf("Erreur ouverture CSV\n");
        return 1;
    }
    fprintf(csv, "Size,Algo,BestCase,PireCase\n");
    
    srand(time(NULL));
    
    for (int s = 0; s < count; s++) {
        int n = sizes[s];
        printf("\n--- Taille %d ---\n", n);
        fflush(stdout);
        
        int *tab = malloc(n * sizeof(int));
        
        /*===============================================
            1) NON TRIE
        ================================================*/
        double totalBest1 = 0, totalWorst1 = 0;
        
        // Générer le tableau une seule fois pour ce test
        for (int i = 0; i < n; i++) 
            tab[i] = rand() % (n * 10);
        
        for (int r = 0; r < outerReps; r++) {
            // BestCase : élément au début
            totalBest1 += measure(rechElets_TabNonTries, tab, n, tab[0], innerReps);
            
            // PireCase : élément inexistant
            totalWorst1 += measure(rechElets_TabNonTries, tab, n, -1, innerReps);
        }
        
        fprintf(csv, "%d,NonTries,%.10f,%.10f\n", n, 
                totalBest1 / outerReps, totalWorst1 / outerReps);
        printf("NonTries - Best: %.10f, Worst: %.10f\n",
               totalBest1 / outerReps, totalWorst1 / outerReps);
        
        /*===============================================
            2) TRIE
        ================================================*/
        double totalBest2 = 0, totalWorst2 = 0;
        
        // Tableau trié
        for (int i = 0; i < n; i++)
            tab[i] = i * 2;
        
        for (int r = 0; r < outerReps; r++) {
            totalBest2 += measure(rechElets_TabTries, tab, n, tab[0], innerReps);
            totalWorst2 += measure(rechElets_TabTries, tab, n, -1, innerReps);
        }
        
        fprintf(csv, "%d,Tries,%.10f,%.10f\n", n, 
                totalBest2 / outerReps, totalWorst2 / outerReps);
        printf("Tries    - Best: %.10f, Worst: %.10f\n",
               totalBest2 / outerReps, totalWorst2 / outerReps);
        
        /*===============================================
            3) DICHO
        ================================================*/
        double totalBest3 = 0, totalWorst3 = 0;
        
        // Même tableau trié
        for (int i = 0; i < n; i++)
            tab[i] = i * 3;
        
        for (int r = 0; r < outerReps; r++) {
            // BestCase : élément au milieu
            totalBest3 += measure(rechElets_Dicho, tab, n, tab[n/2], innerReps);
            // PireCase : élément inexistant
            totalWorst3 += measure(rechElets_Dicho, tab, n, -1, innerReps);
        }
        
        fprintf(csv, "%d,Dicho,%.10f,%.10f\n", n, 
                totalBest3 / outerReps, totalWorst3 / outerReps);
        printf("Dicho    - Best: %.10f, Worst: %.10f\n",
               totalBest3 / outerReps, totalWorst3 / outerReps);
        
        free(tab);
    }
    
    fclose(csv);
    printf("\n✓ Fichier sizes.csv généré avec succès.\n");
    return 0;
}
