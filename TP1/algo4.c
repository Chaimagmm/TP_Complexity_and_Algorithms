#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


int main(){
int n, i, premier;
premier = 1;

clock_t debut, fin;
printf(" Enter un numero que vous voulez tester ca primalite :\n");
scanf("%d", &n);
debut =  clock();
if(n == 2)
   premier = 1;
else if((n%2)==0)
   premier = 0;
else{
    i = 3;
    while(i <= (int)sqrt(n) && premier ==1 ){
       if((n % i) == 0)
         premier = 0;
       else
         i= i+2;
    }
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