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

void bubble(int a[],int n)
{
    int i = 0,j = 0,flag = 0;
    for (i = n-1;i > 0;i--) {
        flag = 1;
        for (j = 0; j < i ;j++) {
            if (a[j] > a[j + 1]) {
                swap(&a[j],&a[j+1]);
                flag = 0;
            }
        }
        if (flag == 1) {
            break;
        }
    }
}

int main()
{
    int a[5] = {10,4,20,30,6};
    bubble(a, 5);
    p(a, 5);
    return 0;
}

