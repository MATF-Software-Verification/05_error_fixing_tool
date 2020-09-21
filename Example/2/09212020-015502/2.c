#include <stdio.h>
#include <stdlib.h>

int main()
{
  char *p, q;

  p = (char *) malloc(19);
  p = (char *) realloc(p, 12);
  free(p);


  p = &q;

  				
  return 0;
}
