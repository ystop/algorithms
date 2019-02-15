#include<stdio.h>
#include<stdlib.h>

int fib(int n)
{
    if (n == 0 || n == 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int fib1(int n) 
{
    int a = 0, b = 1;
    int index, sum;
    if (n == 0 || n == 1) {
        return n;
    }
    for (index = 2;index <= n;index++) {
        sum = a + b;
        a = b;
        b = sum;
    }
    return sum;
}


int main(void) 
{
    printf("%d\n",fib(10));
    printf("%d\n",fib1(10));
    return 0;
}

