package test;

import java.util.Scanner;

public class cube{
	void display(double x[][],int e)
	{
		for(int i=0;i<x.length;i++)
		{
			x[i][i]-=e;
		}
		for(int i=0;i<x.length;i++)
		{
			for(int j=0;j<x.length;j++)
			{
				System.out.print(x[i][j]+"\t");
			}
			System.out.println();
		}
	}
			public static void main(String args[])
			{
					cube c=new cube();
					Scanner s=new Scanner(System.in);
					System.out.println("Enter the Order of Square matrix : ");
					int n=s.nextInt();
					double x[][]=new double[n][n];
					System.out.println("Enter the elements Row-wise : ");
					for(int i=0;i<n;i++)
					{
						for(int j=0;j<n;j++)
						{
							x[i][j]=s.nextDouble();
						}
					}
					c.display(x,2);
			}
}