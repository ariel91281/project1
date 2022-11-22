
#include <stdio.h>

struct print_me
{ 
        int value; 
        void (*Print) (int n); 
}; 
void PrintThis (int n)
{ 
        printf("print from struct : %d\n",n); 
}


int main()
{
        struct print_me array[10];
        int i;
        for(i=0; i<10 ;i++)
	{
                array[i].value = i + 1;
                array[i].Print = PrintThis;
                array[i].Print(array[i].value);
        }

        return 0;
}
