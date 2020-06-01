#include <stdio.h>
#include <stdlib.h>
int main (int argc, char *argv[]) 
/*arcg: cantidad de parámetros contando el nombre del ejecutable que es el primer parámetro.

argv[]: Un apuntador que contiene todos los parámetros recibidos.*/
{
int tokens;
for (tokens=0; argv[tokens]!= NULL; tokens++){
	//mientras que el parámetro no sea nulo
if (argv[tokens][0]=='-')
//de la palabra toma el primer caracter/
printf ("opcion: %s,\n", argv[tokens]+1);
else
    printf("argumento %d: %s \n", tokens, argv[tokens]);


}
exit(0);

}