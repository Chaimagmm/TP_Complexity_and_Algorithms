#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rechElets_TabTries(int tab[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return 1;
        else if (tab[i] > x)
            return 0;
    }
    return 0;
}

double get_time_diff(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

int main() {
    FILE *f_tailles = fopen("tailles.txt", "r");
    FILE *f_res = fopen("resultats_trie.csv", "w");
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

        for (int i = 0; i < n; i++)
            tab[i] = i * 2;

        struct timespec start, end;
        double temps_meilleur = 0, temps_pire = 0;
        int repetitions = 1000;  // répéter pour fiabiliser les mesures

        // Meilleur cas
        int x_meilleur = tab[0];
        for (int i = 0; i < repetitions; i++) {
            clock_gettime(CLOCK_MONOTONIC, &start);
            rechElets_TabTries(tab, n, x_meilleur);
            clock_gettime(CLOCK_MONOTONIC, &end);
            temps_meilleur += get_time_diff(start, end);
        }
        temps_meilleur /= repetitions;

        // Pire cas
        int x_pire = -1;
        for (int i = 0; i < repetitions; i++) {
            clock_gettime(CLOCK_MONOTONIC, &start);
            rechElets_TabTries(tab, n, x_pire);
            clock_gettime(CLOCK_MONOTONIC, &end);
            temps_pire += get_time_diff(start, end);
        }
        temps_pire /= repetitions;

        fprintf(f_res, "%d,%.10f,%.10f\n", n, temps_meilleur, temps_pire);
        free(tab);
    }

    fclose(f_tailles);
    fclose(f_res);
    printf("Mesures terminées avec précision nanoseconde !\n");
    return 0;
}

