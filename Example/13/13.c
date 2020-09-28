#include <stdio.h>
#include <stdlib.h>

int main () {
	int *p = malloc(1);
	p = malloc(10);
	p = malloc(5);
   
	
	p[0] = 10;
	
   	return 0;
}
