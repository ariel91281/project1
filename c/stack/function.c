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
        *pstack->maxsize = capacity;
        *pstack->top = -1;
        *pstack->items = (int*)malloc(sizeof(int) * capacity);
}

stack_t StackDestroy(stack_t *pstack)
{
	


int StackIsEmpty(stack_t *pstack)
{
	if(*pstack->p ==  0)
	{
		printf("your stack is empty");
		return 1;
	}
	printf("your stack isn't empty");
	return 0;
}


