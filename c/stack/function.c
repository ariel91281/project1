extern int error_i;
typedef struct stack_t stack_t;
stack_t *StackCreate(int stack_size);
int StackDestroy(stack_t *pstack);
int StackPop(struct_t *pstack);
int StackPeek(stack_t *pstack);
int StackIsEmpty(stack_t *pstack);
int StackPush (stack_t *pstack, int element);
int StackSize(stack_t *pstack);
int StackSizeLeft(stack_t *pstack);

struct stack	
{
    int maxsize;  
    int top;
    int *items;
}

stack_t  *StackCreate(int maxsize)
{
	stack *pstack = (stack*)malloc(sizeof(stack) *1;
        *pstack->maxsize = 
        *pstack->top = -1;
        *pstack->items = (int*)malloc(sizeof(int) * capacity);
	return pstack;
}

stack_t StackDestroy(stack_t *pstack)
{
	if(pstack == NULL)
		return 0;
	free(pstack);
	free(pstack->items);
	return 1;
}

int StackIsEmpty(stack_t *pstack)
{
	if(*pstack->top == -1)
	{
		printf("your stack is empty");
		return 1;
	}
	printf("your stack isn't empty");
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
}

int StackPush(stack_t *pstack, int element)
{
	if(pstack->top == pstack->maxsize)

		return 0;
	pstack->items[pstack->top] = element;
	pstack->top++;
}

int StackPeek(stack_t *pstack);
{
	if(StackIsEmpty(pstack) == 1)
		return 0;
	return  pstack->items[pstack->top]; 
}
