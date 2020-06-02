package test;

import java.util.*;

public class derangement {
	int D(int n)
	{
		if(n<=1)
			return 0;
		else if(n==2)
			return 1;
		else
			return (n-1)*(D(n-1)+D(n-2));
	}
	public static void main(String[] args) {
		derangement d=new derangement();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the value of n : ");
		int n=s.nextInt();
		System.out.print("Derangement of "+n+" is "+d.D(n));
		s.close();
	}
}
