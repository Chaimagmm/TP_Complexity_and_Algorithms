#include <stdio.h>
#include <unistd.h> // fork
#include <stdlib.h> // exit
#include <sys/wait.h>

int main()
{
int  pid, statut,resultat;
//tableau qui stock les ids des fils
int pid_fils[3];
resultat = 0;
for(int i=0; i<3; i++){
pid= fork();
if (pid == - 1)
{ /* code si échec : */
perror ( "fork") ;
exit(1) ; //sortir sur un code d’erreur
}
if (pid==0)
{
// Code du fils
if(i==0)
     exit(5);
else if(i==1)
     exit(10);
else
     exit(3);
// Fin du processus fils
}else{
// Suite code du père, si pid > 0
pid_fils[i]= pid;
}
}
for (int i = 0; i < 3; i++) {
    waitpid(pid_fils[i], &statut, 0);
    int val = WEXITSTATUS(statut);
    printf("Le fils %d (pid=%d) a retourné %d\n", i+1, pid_fils[i], val);
    if (val == 3)
        resultat = val * 10 + 5;
}
    
    printf("\nRésultat final :  %d\n", resultat);

    return 0;
}

