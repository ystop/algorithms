#include<stdio.h>
#include<stdlib.h>

void p(int a[], int n)
{
    int i = 0;
    for (i = 0;i < n;i++) {
        printf("%d",a[i]);
        printf("\n");
    }
}

void swap(int *a, int *b)
{
    if (*a != *b)
    {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}

void insert(int a[],int n)
{
    int i = 0;
    int j = 0;
    int min;
    for (i = 1; i< n;i++) {
        if (a[i] < a[i-1]) {
            j = i;
            min = a[i];
            while (j > 0 && (min < a[j-1])) {
                swap(&a[j], &a[j-1]);
                j--; 
            }
        }
    }
}

int main()
{
    int a[9] = {111111,10,4,20,30,6,22,13,3212};
    insert(a, 9);
    p(a, 9);
    return 0;
}

