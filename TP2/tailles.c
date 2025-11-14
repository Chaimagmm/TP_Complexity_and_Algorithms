#include <stdio.h>

int main() {
    FILE *f = fopen("tailles.txt", "w");
    if (!f) return 1;

    int nb_valeurs = 400;      // nombre de tailles à générer
    int n_max = 1800000;       // borne supérieure de l’intervalle
    int n_min = 1;             // borne inférieure

    for (int i = 0; i < nb_valeurs; i++) {
        int taille = n_min + i * (n_max - n_min) / (nb_valeurs - 1);
        fprintf(f, "%d\n", taille);
    }

    fclose(f);
    return 0;
}

