#include <stdio.h>
int funcex2();
int  main()
{
	funcex2(3);
}

int funcex2(int n)
{
	int x=10;
	int i=0;
	int result=1;
	for(i=0;i<n;i++)
	{
        	result=result*x;
	}
	printf("%d\n",result);
	return result;	
}
