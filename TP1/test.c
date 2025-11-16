#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <limits.h>

// Algorithme 1: Test jusqu'à n-1
int test_primalite_1(long long n) {
    long long i = 2;
    int premier = 1;
    while(i <= (n-1) && premier == 1) {
        if((n % i) == 0)
            premier = 0;
        else
            i++;
    }
    return premier;
}

// Algorithme 2: Test jusqu'à n/2
int test_primalite_2(long long n) {
    long long i = 2;
    int premier = 1;
    while(i <= (n/2) && premier == 1) {
        if((n % i) == 0)
            premier = 0;
        else
            i++;
    }
    return premier;
}

// Algorithme 3: Test jusqu'à sqrt(n)
int test_primalite_3(long long n) {
    long long i = 2;
    int premier = 1;
    long long limite = (long long)sqrt(n);
    while(i <= limite && premier == 1) {
        if((n % i) == 0)
            premier = 0;
        else
            i++;
    }
    return premier;
}

// Algorithme 4: Optimisé (saut de 2)
int test_primalite_4(long long n) {
    int premier = 1;
    
    if(n == 2)
        premier = 1;
    else if((n % 2) == 0)
        premier = 0;
    else {
        long long i = 3;
        long long limite = (long long)sqrt(n);
        while(i <= limite && premier == 1) {
            if((n % i) == 0)
                premier = 0;
            else
                i = i + 2;
        }
    }
    return premier;
}

int main() {
    FILE *input_file = fopen("Test-3.txt", "r");
    FILE *output_file = fopen("resultats.csv", "w");
    
    if(input_file == NULL || output_file == NULL) {
        printf("Erreur d'ouverture des fichiers!\n");
        return 1;
    }
    
    // En-tête du fichier CSV
    fprintf(output_file, "Nombre,Chiffres,Algo1,Algo2,Algo3,Algo4\n");
    
    long long n;
    int count = 0;
    
    while(fscanf(input_file, "%lld", &n) != EOF) {
        count++;
        
        // Compter le nombre de chiffres
        long long temp = n;
        int chiffres = 0;
        while(temp != 0) {
            chiffres++;
            temp /= 10;
        }
        
        printf("Traitement du nombre #%d: %lld (%d chiffres)\n", count, n, chiffres);
        
        fprintf(output_file, "%lld,%d,", n, chiffres);
        
        // Tester avec les 4 algorithmes
        for(int algo = 1; algo <= 4; algo++) {
            clock_t debut, fin;
            double temps;
            int premier;
            
            debut = clock();
            
            switch(algo) {
                case 1: premier = test_primalite_1(n); break;
                case 2: premier = test_primalite_2(n); break;
                case 3: premier = test_primalite_3(n); break;
                case 4: premier = test_primalite_4(n); break;
            }
            
            fin = clock();
            temps = ((double)(fin - debut)) / CLOCKS_PER_SEC;
            
            fprintf(output_file, "%.6f", temps);
            if(algo < 4) fprintf(output_file, ",");
            
            printf("  Algo%d: %.6f sec - %s\n", algo, temps, premier ? "premier" : "non premier");
        }
        fprintf(output_file, "\n");
    }
    
    fclose(input_file);
    fclose(output_file);
    printf("\nTraitement terminé! %d nombres traités.\n", count);
    printf("Résultats sauvegardés dans resultats.csv\n");
    
    return 0;
}
