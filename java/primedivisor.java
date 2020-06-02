package algebra;

import java.util.Scanner;

public class primedivisor {
	int p=0,j;
	void div(int x)
	{
		System.out.println("Prime divisors of "+x+" are");
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
		System.out.println("Total : "+p);
	}
	public static void main(String args[])
	{
		Scanner s=new Scanner(System.in);
		primedivisor d=new primedivisor();
		System.out.print("Enter the number : ");
		int x=s.nextInt();
		d.div(x);
		s.close();
	}
}
