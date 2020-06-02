package test;

public class function{
	static int max(int x[],int n)//maximum of n numbers 
	{
		int m=x[0];
			for(int i=0;i<n;i++)
			{
				if(x[i]>m)
				{
					m=x[i];
				}
			}
			return m;
	}
	static int sum(int n)//sum of digits of a number
	{
		int s=0;
		while(n>0)
		{
			s+=n%10;
			n=n/10;
		}
		return s;
	}
	static int gcd(int x,int y)//gcd of two numbers
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
	static int pdc(int x)//count prime divisors
	{
		int p=0,j;
		for(int i=2;i<=x;i++)
		{
			if(x%i==0)
			{
				for(j=2;j<=i;j++)
				{
					if(i%j==0)
					break;
				}
				if(i==j)
				{
					System.out.println(i);
					p++;
				}
			}		
		}
		return p;
	}
	static int mult(int x,int y)//multiplicity of a divisor
	{
		int c=0;
		while(x%y==0)
		{
			x=x/y;
			c++;
		}
		return c;
	}
	static int fact(int x)//factorial
	{
		if(x<=1)
			return 1;
		else
			return x*fact(x-1);			
	}
}
