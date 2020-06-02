package test;

import java.util.*;

public class GenPrfctNo {
	boolean pc(int x)
	{
		int i;
		for(i=2;i<=x;i++)
		{
			if(x%i==0)
			break;
		}
		if(i==x)
			return true;
		else
			return false;
	}
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		GenPrfctNo t=new GenPrfctNo();
		System.out.print("Enter the number :");
		int n=s.nextInt();
		System.out.println("The perfect numbers are :");
		for(int i=2;i<=n;i++)
		{
			if(t.pc((int)Math.pow(2, i)-1))
			System.out.println((int)((Math.pow(2, i)-1)*Math.pow(2,i-1)));
		}
		s.close();
	}
}
