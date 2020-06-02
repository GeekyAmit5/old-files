package test;

import java.util.*;

public class fact{
	public static void main(String args[]){
	Scanner s=new Scanner(System.in);
	System.out.println("Enter the number : ");
	int n=s.nextInt();
	System.out.println("Fatorial of "+n+" is "+fact(n));
	}
	static int fact(int x)//factorial
	{
		if(x<=1)
			return 1;
		else
			return x*fact(x-1);			
	}
}