#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
int n, i, premier;
premier = 1;
i = 2;
printf(" Enter un numero que vous voulez tester ca primalite :\n");
scanf("%d", &n);
    while(i <= (int)sqrt(n-1) && premier ==1 ){
       if((n % i) == 0)
         premier = 0;
       else
         i++;
    }
if(premier == 1)
  printf(" %d est premier \n", n);
else 
  printf(" %d n'est pas premier \n", n);
return 0;

}
