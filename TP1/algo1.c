#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){
int n, i, premier;
premier = 1;
i = 2;
clock_t debut, fin;
printf(" Enter un numero que vous voulez tester ca primalite :\n");
scanf("%d", &n);
debut =  clock();
    while(i <= (n-1) && premier ==1 ){
       if((n % i) == 0)
         premier = 0;
       else
         i++;
    }
fin = clock();
double temps = ((double)(fin - debut)) / CLOCKS_PER_SEC;
    if(premier == 1)
    printf(" %d est prmier \n", n);
    else 
    printf(" %d n'est pas prmier \n", n);
printf("Temps d'execution : %f secondes\n", temps);


return 0;

}