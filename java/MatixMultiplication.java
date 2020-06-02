package algebra;

import java.util.*;
 
public class MatixMultiplication{
	void display(int a[][],int b[][],int p)
	{
		System.out.println("The First Matrix is :");
		for(int i=0;i<a.length;i++)
		{
			for(int j=0;j<b.length;j++)
			{
				System.out.print(a[i][j]+"\t");
			}
			System.out.println();
		}
		System.out.println("The Second Matrix is :");
		for(int i=0;i<b.length;i++)
		{
			for(int j=0;j<p;j++)
			{
				System.out.print(b[i][j]+"\t");
			}
			System.out.println();
		}
	}
	void product(int x[][],int y[][],int p)
	{
		int c[][]=new int[x.length][p];
		for(int i=0;i<x.length;i++)
		{
			for(int j=0;j<p;j++)
			{
				for(int k=0;k<y.length;k++)
				{
					c[i][j]+=x[i][k]*y[k][j];
				}
			}
		}
		System.out.println("The Product Matrix is :");
		for(int i=0;i<x.length;i++)
		{
			for(int j=0;j<p;j++)
			{
				System.out.print(c[i][j]+"\t");
			}
			System.out.println();
		}
	}
    public static void main(String args[]) {
    MatixMultiplication m=new MatixMultiplication();
    Scanner s=new Scanner(System.in);
	System.out.println("Enter The Order of First Matrix: ");
	int m1=s.nextInt();
	int n1=s.nextInt();
	int a[][]=new int[m1][n1];
	System.out.println("Enter The Elements Row-wise: ");
	for(int i=0;i<m1;i++)
	{
		for(int j=0;j<n1;j++)
		{
			a[i][j]=s.nextInt();
		}
	}
	System.out.println("Enter The Order of Second Matrix : ");
	int m2=s.nextInt();
	int n2=s.nextInt();
	int b[][]=new int[m2][n2];
	System.out.println("Enter The Elements Row-wise :");
	for(int i=0;i<m2;i++)
	{
		for(int j=0;j<n2;j++)
		{
			b[i][j]=s.nextInt();
		}
	}
	if(n1==m2)
	{
		m.display(a,b,n2);
		m.product(a,b,n2);
	}
	else
		System.out.println("Product is not possible !");
	s.close();
	}
}
