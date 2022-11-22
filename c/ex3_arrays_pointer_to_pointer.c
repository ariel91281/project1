#include <stdio.h>

int main()
{
	int a;
	printf("size of short int = %lu\n",sizeof((short int) a));
	printf("size of unsigned short int = %lu\n",sizeof((unsigned short int)a));
	printf("size of unsigned int = %lu\n",sizeof((unsigned int)a));
	printf("size of int = %lu\n",sizeof((int)a));
	printf("size of long int = %lu\n",sizeof((long int )a));
	printf("size of unsigned long int = %lu\n",sizeof((unsigned long int)a));
	printf("size of long long int = %lu\n",sizeof((long long int)a));
	printf("size of unsigned long long int = %lu\n",sizeof((unsigned long long int)a));
	printf("size of signed char = %lu\n",sizeof((signed char)a));
	printf("size of unsigned char = %lu\n",sizeof((unsigned char)a));
	printf("size of float = %lu\n",sizeof((float)a));
	printf("size of double = %lu\n",sizeof((double)a));
	printf("size of long double = %lu\n",sizeof((long double)a));
}


	
	
