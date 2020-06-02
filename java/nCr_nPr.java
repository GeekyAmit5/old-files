package test;

import java.util.*;

public class nCr_nPr {
	int fact(int x)
	{
		if(x<=1)
			return 1;
		else
			return x*fact(x-1);			
	}
	int N(int n,int r)//by recursion 
	{
		if(r==0||r==n)
			return 1;
		else 
			return N(n-1,r-1)+N(n-1,r);
	}
	public static void main(String[] args) {
		nCr_nPr c=new nCr_nPr();
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the value of n and r : ");
		int n=s.nextInt();
		int r=s.nextInt();
		System.out.println(n+"C"+r+" is "+c.N(n,r)+"\n"+n+"P"+r+" is "+c.fact(n)/c.fact(n-r));//by factorial
		s.close();
	}
}
