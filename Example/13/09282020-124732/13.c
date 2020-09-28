#include <stdio.h>
#include <stdlib.h>

int main () {
	int *p = malloc(1);
	free(p);
	p = malloc(10);
	free(p);
	p = malloc(5);
   
	
	p[0] = 10;
	
	free(p);
   	return 0;
}
