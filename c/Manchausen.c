#include<stdio.h>
#include<conio.h>
#include<math.h>

void main()
{
	int n,c=0,i;
	printf("Enter the upper bound :");
	scanf("%d",&n);
	printf("The Manchaunsen Numbers Upto %d are:",n);
	for(i=1;i<=n;i++)
	{
		if (isManchausen(i))
		{
			printf(i);
			c++;
		}
	}
	printf("Total:%d",c);
}

int[] digit_list(x)
{
	int a[len(x)],i=0;
	while(x>0)
    {
        a[i]=x%10;
        x/=10;
        i++;
    }
    return a;
}

int len(x)
{
    int l=0;
    while(x>0)
    {
        x/=10;
        l++;
    }
    return l;
}

bool isManchausen(x)
{
    int i=0,s=0;
	for(i=0;i<=len(x);i++)
    {
        s+=pow(digit_list(x)[i],digit_list(x)[i]);
    }
    if (x==s)
        return true;
    return false;
}
