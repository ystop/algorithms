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


void sel(int a[], int n)
{
    int i, j = 0;
    int min = 0;
    int min_index = 0;
    int now_index = 0;
    for (i = 0; i < n - 1; i++) {
        min = a[i];
        min_index = i;
        for (j = i+1; j < n; j++) {
            if (a[j] < min) {
                min = a[j];
                min_index = j;
            }
        }
        swap(&a[i],&a[min_index]);
    }

}

int main()
{
    int a[5] = {10,4,20,30,6};
    sel(a, 5);
    p(a, 5);
}

