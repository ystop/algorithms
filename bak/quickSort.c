#include<stdio.h>
int AdjustArray(int s[], int l, int r)
{
    int i = l,j = r;
    int x = s[l];
    while (i < j) {
        while (i < j && s[j] >= x) {
            j--;
        }
        if (i < j) {
            s[i] = s[j];
            i++;
        }
        while (i < j && s[i] < x) {
            i++;
        }
        if (i < j) {
            s[j] = s[i];
            j--;
        }
    }
    s[i] = x;
    return i;
}
void quick_sort(int s[], int l,int r)
{
    if (l<r)
    {
        int i = AdjustArray(s, l ,r);
        quick_sort(s, l , i-1);
        quick_sort(s, i+1 ,r);
    }
}


int main()
{
    int arr[] = {8,2,4,5,9,7};
    int i;
    quick_sort(arr, 0 ,5);
    for (i =0 ;i< 6; i++)
    {
        printf("%d",arr[i]);
    }
}
