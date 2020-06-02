#include <stdio.h>

    int main()
	{
        int x,y,gcd();
        printf("Enter the Numbers :\n");
        scanf("%d %d",&x,&y);
        printf("GCD of %d and %d is : %d\n",x,y,gcd(x,y));
        printf("LCM of %d and %d is : %d\n",x,y,(x*y)/gcd(x,y));
	}
	int gcd(int x,int y)
	{
	    int r;
	    while(y>0)
        {
            r=x%y;
            x=y;
            y=r;
        }
        return x;
	}
