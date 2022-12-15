#include <stdio.h>
#include "head.h"
#include <stdlib.h>

struct stack_t
{
	int maxsize;
	int top;
	int *items;
};

stack_t  *StackCreate(int num_of_elements)
{
	stack_t *pstack = (stack_t*)malloc(sizeof(stack_t) + sizeof(int)*num_of_elements) ;
	pstack->maxsize = (num_of_elements*sizeof(int));
        pstack->top = -1;
	//pstack->items = (int*)malloc(sizeof(int)*num_of_elements);
	int *temp = (int *)pstack;
	pstack->items = temp + (sizeof(int));
	return pstack;
}

int StackDestroy(stack_t *pstack)
{
	if(pstack == NULL)
		return 0;
	free(pstack);
	return 1;
}

int StackIsEmpty(stack_t *pstack)
{
	if(pstack->top == -1)
	{
		return 1;
	}
	return 0;
}


int StackPop(stack_t *pstack)
{
	error_i = 1;
	if(StackIsEmpty(pstack) == 1)
	{
		 error_i = 0;
		 return error_i;
	}
	pstack->top--;
	return pstack->items[pstack->top+1];
}

int StackPush(stack_t *pstack, int element)
{
	//if(((pstack->top)+1) * sizeof(int) == pstack->maxsize)
	if(pstack->top == pstack->maxsize) 
	return 0;
	if (StackIsEmpty(pstack))
	pstack->top = 0;
	pstack->items[pstack->top] = element;
	pstack->top++;
	return 1;
}

int StackPeek(stack_t *pstack)
{
	if(StackIsEmpty(pstack) == 1)
		return 0;
	return  pstack->items[pstack->top-1];
}

int StackSize(stack_t *pstack)
{
	long size;
	error_i = 1;
	if(pstack == NULL)//check if pointer points to null
		return error_i = 0;
	size = pstack->top  * sizeof(int);
	if(size < 0)
		return 0;
	return pstack->top  * sizeof(int);
}


int StackSizeLeft(stack_t *pstack)
{
	 error_i = 1;
	if(pstack == NULL)//check if pointer points to null
		return error_i = 0;
	return pstack->maxsize - StackSize(pstack);
}

