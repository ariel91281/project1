#include <stdio.h>
void copyArray(int arr[], int copy[], int size)
{
  for (i = 0; i < size; ++i)
  {
    copy[i] = arr[i];
  }
}

int main()
{
  int i = 0;
  int arr[] = {10, 20, 30, 40, 50};
  int size = sizeof(arr)/sizeof(arr[0]);
  int newArr[size];
  copyArray(arr, newArr, size);
  printf("Original array = ");
  displayArray(arr, size);
  return 0;
}
