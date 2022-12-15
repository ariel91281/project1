#include <stdio.h>
#include "head.h"
int main()
{
	int i = 0;
	stack_t *st = StackCreate(10);
	int size = StackSizeLeft(st);
	printf("size = %d\n",size);
	if(40 == size)
		printf("success\n");
	else
		printf("failed\n");
	printf("Push test\n");
	for(i=0 ; i<11; i++)
	{
	if(StackPush(st,i) == 1)
		printf("success\n");
	else
		printf("failed\n");
	printf("%d\n",StackPeek(st));
	}
	printf("Pop test:\n");
	for(i=10 ;i>=0 ; i--)
	{
		printf("%d\n",StackPeek(st));
		if(i == StackPop(st))
			printf("success\n");
		else
			printf("failed\n");
	}
	return 0;
}
