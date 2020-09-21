#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *p;
	int * q;
	p= (char *) malloc(abs(-10));

	q = (int *) malloc(abs(-15*sizeof(int)));

	p = (char *) realloc(p,abs( -50));

	p[0] = 'a';
	q[0] = 2;

	free(p);
	free(q);
	return 0;
}
