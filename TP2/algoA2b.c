#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rechElets_Dicho(int tab[], int n, int x) {
    int debut = 0, fin = n - 1, milieu;

    while (debut <= fin) {
        milieu = (debut + fin) / 2;

        if (tab[milieu] == x)
            return 1;
        else if (tab[milieu] < x)
            debut = milieu + 1;
        else
            fin = milieu - 1;
    }
    return 0;
}

int main() {
    int n, x, *tab;
    clock_t t1, t2;

    printf("Entrez la taille du tableau : ");
    scanf("%d", &n);
    tab = (int*) malloc(n * sizeof(int));

    // Remplissage trié
    for (int i = 0; i < n; i++)
        tab[i] = i * 3;

    printf("Entrez l'élément à rechercher : ");
    scanf("%d", &x);

    t1 = clock();
    int trouve = rechElets_Dicho(tab, n, x);
    t2 = clock();

    double temps = (double)(t2 - t1) / CLOCKS_PER_SEC;
    printf("%d %s dans le tableau.\n", x, trouve ? "existe" : "n'existe pas");
    printf("Temps d'exécution : %f secondes\n", temps);

    free(tab);
    system("pause");
    return 0;
}
