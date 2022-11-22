#include <stdio.h>

void swap (int *x, int *y)
{
  int temp;
  temp = *x;
  *x = *y;
  *y = temp;
} 

void main()
{
	int var1 = 5;
	int var2 = 8;
	swap(&var1,&var2);
	printf("%d\n",var1);
	printf("%d\n",var2);
}
