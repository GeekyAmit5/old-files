#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include<math.h>

int isPrime(int n)
{
    for(int i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return i;
    return n;
}

int main()
{
    int n;
    clock_t t0,t1;
    printf("Enter The Upper Bound : ");
    scanf("%d",&n);
    t0=clock();
    printf("The Prime Numbers Upto %d are \n",n);
    for(int i=2;i<=n;i++)
        if (isPrime(i)==i)
            printf("%d\n",i);
    t1=clock();
    printf("Time : %f",(t1-t0)/(double)CLOCKS_PER_SEC);
    return 0;
}
