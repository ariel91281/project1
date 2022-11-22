#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv, char **buffer)
{
  for (char **env = buffer; *env != 0; env++)
  {
    
    char *thisEnv = *env;
    while(*thisEnv)
    {
    	printf("%c", (char)tolower(*thisEnv));
    	    
    	thisEnv++;
    }
    printf("\n");
  }
  return 0;
}

