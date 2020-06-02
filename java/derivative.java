package test;

import java.util.*;

public class derivative {
	void d(int x[],int n)
	{
		System.out.println("The derivative of the given polynomial is : ");
		System.out.print(x[1]);
		System.out.print(" + "+x[2]*2+"x");
		for(int i=3;i<n+1;i++)
		{
			x[i]*=i;
			System.out.print(" + "+x[i]+"x^"+(i-1));
		}
	}
	public static void main(String[] args) {
		derivative d=new derivative();
		Scanner s =new Scanner(System.in);
		System.out.print("Enter the degree of the polynomial : ");
		int n=s.nextInt();
		System.out.println("Enter the Coefficient of the polynomial : ");
		int x[]=new int[n+1];
		for(int i=0;i<(n+1);i++)
		{
			x[i]=s.nextInt();
		}
		d.d(x,n);
		s.close();
	}
}
