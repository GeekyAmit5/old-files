package test;

import java.util.Scanner;

public class geometricseries {
	private static Scanner s;
	double sum=0;
	double r;
	double sum(int n)
	{
			for(int i=0;i<=n;i++)
			{
				sum+=power(i);
			}
			return sum;
	}
	double power(int x)
	{
		double y=1;
		if(x==0)
			return 1;
		else
			for(int i=1;i<=x;i++)
			{
				y*=r;
			}
			return y;
	}
	public static void main(String args[])
	{
			geometricseries g =new geometricseries();
			s=new Scanner(System.in);
			System.out.print("Enter the value of common ratio : ");
			g.r=s.nextDouble();
			System.out.println("Sum is "+g.sum(10000));
	}
}

