#include <stdio.h>
#include <stdlib.h>

int main() {

    // Les tailles demandées
    int sizes[] = {
        100000, 200000, 400000, 600000, 800000,
        1000000, 1200000, 1400000, 1600000, 1800000,
        2000000,
        4000000, 5000000, 6000000, 7000000, 8000000
    };

    int count = sizeof(sizes) / sizeof(sizes[0]);

    // Ouvrir le fichier CSV
    FILE *file = fopen("sizes.csv", "w");
    if (file == NULL) {
        printf("Erreur : impossible de créer le fichier CSV.\n");
        exit(1);
    }

    // Écrire l’en-tête
    fprintf(file, "Size\n");

    // Sauvegarder les tailles
    for (int i = 0; i < count; i++) {
        fprintf(file, "%d\n", sizes[i]);
    }

    fclose(file);

    printf("Fichier sizes.csv généré avec succès.\n");

    return 0;
}

