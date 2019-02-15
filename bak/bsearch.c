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

int b_search(int a[],int n, int key)
{
    int low = 0;
    int high = n;
    int mid;
    while (low <= high) {
        mid = (low+high)/2;
        if (key > a[mid]) {
            low = mid+1;
        } else if (key < a[mid]) {
            high = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}

int main()
{
    int a[5] = {1,2,3,4,5};
    int b = b_search(a,4,2);
    printf("%d", b);
    return 0;
}

