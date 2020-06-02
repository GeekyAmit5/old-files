package test;

import java.util.*;

public class expansion {
	int nCr(int n,int r)
	{
		if(r==0||r==n)
			return 1;
		else 
			return nCr(n-1,r-1)+nCr(n-1,r);
	}
	void exp(int n)
	{
		System.out.print("x^"+n);
		for(int i=1;i<n;i++)
		{
			System.out.print(" + "+nCr(n,i)+"x^"+(n-i)+"y^"+i);
		}
		System.out.print(" + y^"+n);
	}
	public static void main(String[] args) {
		expansion e=new expansion();
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the value of n : ");
		e.exp(s.nextInt());
		s.close();
	}
}
