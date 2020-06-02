package algebra;
import java.util.Scanner;

public class fifunction {
	private static Scanner s;
	int g(int x,int y)
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
	int fi(int n)//using gcd
	{
		int p=0;
		for(int i=1;i<=n;i++)
		{
			if(g(i,n)==1)
			{
				p++;
			}
		}
		return p;
	}
	void alternate(int x)//using prime divisors
	{
		int f=x,j;
		System.out.println(" ");
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
					f*=((j-1)/(double)j);
				}
			}		
		}
		System.out.print("Fi of "+x+" is "+(int)f);
	}
	public static void main(String[] args) 
	{
		fifunction f= new fifunction();
		s=new Scanner(System.in);
		System.out.print("Enter the number : ");
		int n=s.nextInt();
		System.out.println("Fi of "+n+" is "+f.fi(n));
		//f.alternate(n);
	}
}
