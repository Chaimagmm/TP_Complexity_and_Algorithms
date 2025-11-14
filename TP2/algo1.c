#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rechElets_TabNonTries(int tab[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return 1; // trouvé
    }
    return 0; // non trouvé
}

int main() {
    FILE *f_tailles = fopen("tailles.txt", "r");
    FILE *f_res = fopen("resultats1.csv", "w");
    if (!f_tailles || !f_res) {
        printf("Erreur lors de l'ouverture d'un fichier.\n");
        return 1;
    }

    fprintf(f_res, "n,temps_meilleur,temps_pire\n");

    int n;
    srand(time(NULL));

    while (fscanf(f_tailles, "%d", &n) == 1) {
        int *tab = (int*) malloc(n * sizeof(int));
        if (!tab) continue;

        // Remplir le tableau avec des valeurs aléatoires
        for (int i = 0; i < n; i++)
            tab[i] = rand() % (n * 10);

        clock_t debut, fin;
        double temps_meilleur, temps_pire;

        // ---- Meilleur cas (élément au début)
        int x_meilleur = tab[0];
        debut = clock();
        rechElets_TabNonTries(tab, n, x_meilleur);
        fin = clock();
        temps_meilleur = (double)(fin - debut) / CLOCKS_PER_SEC;

        // ---- Pire cas (élément absent)
        int x_pire = -1; // on choisit un nombre qui ne peut pas exister
        debut = clock();
        rechElets_TabNonTries(tab, n, x_pire);
        fin = clock();
        temps_pire = (double)(fin - debut) / CLOCKS_PER_SEC;

        // Sauvegarde des résultats
        fprintf(f_res, "%d,%f,%f\n", n, temps_meilleur, temps_pire);

        free(tab);
    }

    fclose(f_tailles);
    fclose(f_res);
    printf("Mesures terminées. Résultats enregistrés dans resultats.csv\n");
    return 0;
}

