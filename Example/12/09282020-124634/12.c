#include<stdio.h>
#include <stdlib.h>


int  main (){
	
	int *t = malloc( sizeof( int )*5) ;
	t[-100] = 15;
	
	free(t);
	return 0;
}
