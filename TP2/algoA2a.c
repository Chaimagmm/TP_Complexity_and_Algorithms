#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rechElets_TabTries(int tab[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return 1;
        else if (tab[i] > x)
            return 0; // inutile de continuer
    }
    return 0;
}

int main() {
    int n, x, *tab;
    clock_t debut, fin;

    printf("Entrez la taille du tableau : ");
    scanf("%d", &n);
    tab = (int*) malloc(n * sizeof(int));

    // Remplissage trié
    for (int i = 0; i < n; i++)
        tab[i] = i * 2;

    printf("Entrez l'élément à rechercher : ");
    scanf("%d", &x);

    debut = clock();
    int trouve = rechElets_TabTries(tab, n, x);
    fin = clock();

    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    printf("%d %s dans le tableau.\n", x, trouve ? "existe" : "n'existe pas");
    printf("Temps d'exécution : %f secondes\n", temps);

    free(tab);
    system("pause");
    return 0;
}
