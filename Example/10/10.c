#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *p, *q;

	p= (char *) malloc(19);

	q = (char *) malloc(12);

	p = (char *) realloc(p, 50);
  
	p[0] = 'a';
	q[0] = 't';
  	
	return 0;
}
