#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *p;
	int * q;
	p= (char *) malloc(-10);

	q = (int *) malloc(-15*sizeof(int));

	p = (char *) realloc(p, -50);

	p[0] = 'a';
	q[0] = 2;

	return 0;
}
