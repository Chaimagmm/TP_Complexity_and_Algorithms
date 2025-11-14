#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void MaxEtMinA(int tab[], int n, int *max, int *min, int *comparaisons) {
    *max = tab[0];
    *min = tab[0];
    *comparaisons = 0;

    for (int i = 1; i < n; i++) {
        (*comparaisons)++;
        if (tab[i] > *max)
            *max = tab[i];
    }
    for (int i = 1; i < n; i++) {
        (*comparaisons)++;
        if (tab[i] < *min)
            *min = tab[i];
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
    MaxEtMinA(tab, n, &max, &min, &comp);
    fin = clock();

    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    printf("Max = %d, Min = %d\n", max, min);
    printf("Comparaisons : %d\n", comp);
    printf("Temps d'exécution : %f secondes\n", temps);

    free(tab);
    system("pause");
    return 0;
}
