#include<stdio.h>
#include <stdlib.h>


int  main (){
	int x = 3;
	int *t = malloc ( sizeof(int)*8 );
	int __index__;
	for( __index__ = 0; __index__ < 8; __index__ ++)
		t[__index__] = 0;

	t[5] = 15;
	printf("x = %d, t = %d\n",x, t[7]);

	free(t);
	return  0;
}
