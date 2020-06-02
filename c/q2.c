#include<stdio.h>
int isPrime(int);
int main()
{
	int i, n,m;
	FILE *fp;
	printf("Enter the Bounds :\n");
	scanf("%d%d",&m,&n);
	printf("The prime numbers between %d and %d are :\n",m,n);
	fp=fopen("PRIME.txt","w");
	for(i=m;i<=n;i++)
	if(isPrime(i))
    {
        fprintf(fp,"%d\n",i);
        printf("%d\n",i);
    }
	fclose(fp);
	return 0;
}
int isPrime(int x)
{
	int t=1,i;
	for(i=2;i<x;i++)
	{
		if(x%i==0)
		{
			t=0;
			break;
		}
	}
	return t;
}
