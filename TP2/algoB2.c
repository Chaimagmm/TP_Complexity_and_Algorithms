#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/*
void MaxEtMinB(int tab[], int n, int *max, int *min, int *comparaisons) {
    int i = 0;
    *comparaisons = 0;

    if (n % 2 == 0) {
        (*comparaisons)++;
        if (tab[0] > tab[1]) {
            *max = tab[0];
            *min = tab[1];
        } else {
            *max = tab[1];
            *min = tab[0];
        }
        i = 2;
    } else {
        *max = *min = tab[0];
        i = 1;
    }

    while (i < n - 1) {
        (*comparaisons)++;
        int localMax, localMin;
        if (tab[i] > tab[i + 1]) {
            localMax = tab[i];
            localMin = tab[i + 1];
        } else {
            localMax = tab[i + 1];
            localMin = tab[i];
        }
        (*comparaisons) += 2;
        if (localMax > *max) *max = localMax;
        if (localMin < *min) *min = localMin;
        i += 2;
    }
}*/
void MaxEtMinB(int tab[], int n, int *max, int *min, int *comparaisons) {
    *comparaisons = 0;

    // Phase 1: ranger petit en position paire, grand en position impaire
    int i;
    for (i = 0; i + 1 < n; i += 2) {
        (*comparaisons)++;
        if (tab[i] > tab[i + 1]) {
            int tmp = tab[i];
            tab[i] = tab[i + 1];      // case paire = petit
            tab[i + 1] = tmp;         // case impaire = grand
        }
    }

    // Phase 2: chercher le minimum dans les cases paires
    *min = tab[0];
    for (int j = 2; j < n; j += 2) {
        (*comparaisons)++;
        if (tab[j] < *min)
            *min = tab[j];
    }

    // Phase 3: chercher le maximum dans les cases impaires
    if (n > 1)
        *max = tab[1];
    else
        *max = tab[0];

    for (int j = 3; j < n; j += 2) {
        (*comparaisons)++;
        if (tab[j] > *max)
            *max = tab[j];
    }

    // Si n est impair: dernier élément non comparé dans la phase 1
    if (n % 2 == 1) {
        int last = tab[n - 1];

        (*comparaisons)++;
        if (last < *min) *min = last;

        (*comparaisons)++;
        if (last > *max) *max = last;
    }
}


int main() {
    int n, *tab, max, min, comp;
    clock_t debut, fin;

    printf("Entrez la taille du tableau : ");
    scanf("%d", &n);
    tab = (int*) malloc(n * sizeof(int));

    srand(time(NULL));
    for (int i = 0; i < n; i++)
        tab[i] = rand() % (n * 10);

    debut = clock();
    MaxEtMinB(tab, n, &max, &min, &comp);
    fin = clock();

    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    printf("Max = %d, Min = %d\n", max, min);
    printf("Comparaisons : %d\n", comp);
    printf("Temps d'exécution : %f secondes\n", temps);

    free(tab);
    system("pause");

    return 0;
}
