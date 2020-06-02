#include<stdio.h>
#include<math.h>
int main()
{
    int n;
    printf("Enter The Number: ");
    scanf("%d",&n);
    if(isPrime(n))
        printf("%d is Prime Number",n);
    else
        printf("%d is not Prime Number",n);
    return 0;
}
int isPrime(int x)
{
    int i,t=1;
    for(i=2;i<=sqrt(x);i++)
        if(x%i==0)
        {
            t=0;
            break;
        }
        return t;
}
