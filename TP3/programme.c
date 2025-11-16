#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int m1, n1, m2, n2;

    printf("Entrez les dimensions de la matrice A (lignes colonnes) : ");
    scanf("%d %d", &m1, &n1);

    printf("Entrez les dimensions de la matrice B (lignes colonnes) : ");
    scanf("%d %d", &m2, &n2);

    if (n1 != m2) {
        printf("Erreur : A et B sont incompatibles pour la multiplication.\n");
        return 1;
    }

    // Allocation dynamique
    int **A, **B, **R;
    A = malloc(m1 * sizeof(int *));
    B = malloc(m2 * sizeof(int *));
    R = malloc(m1 * sizeof(int *));
    for (int i = 0; i < m1; i++) {
        A[i] = malloc(n1 * sizeof(int));
        R[i] = malloc(n2 * sizeof(int));
    }
    for (int i = 0; i < m2; i++) {
        B[i] = malloc(n2 * sizeof(int));
    }

    srand(time(NULL));

    // Remplissage automatique
    for (int i = 0; i < m1; i++)
        for (int j = 0; j < n1; j++)
            A[i][j] = rand() % 10;

    for (int i = 0; i < m2; i++)
        for (int j = 0; j < n2; j++)
            B[i][j] = rand() % 10;

    // Multiplication
    clock_t start = clock();
    for (int i = 0; i < m1; i++)
        for (int j = 0; j < n2; j++) {
            R[i][j] = 0;
            for (int k = 0; k < n1; k++)
                R[i][j] += A[i][k] * B[k][j];
        }
    clock_t end = clock();

    printf("Temps d'exécution : %f secondes\n",
        (double)(end - start) / CLOCKS_PER_SEC);

    // Libération de la mémoire
    for (int i = 0; i < m1; i++) {
        free(A[i]);
        free(R[i]);
    }
    for (int i = 0; i < m2; i++)
        free(B[i]);
    free(A);
    free(B);
    free(R);

    return 0;
}

