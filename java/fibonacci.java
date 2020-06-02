package test;
import java.util.Scanner;

public class fibonacci {
		int fibo(int a,int b,int n)
		{
			if(n==1)
				return a;
			else if(n==2)
				return b;
			else 
				return fibo(a,b,n-1)+fibo(a,b,n-2);
		}
	public static void main(String args[]){
		Scanner s=new Scanner(System.in);
		fibonacci f=new fibonacci();
		System.out.println("Enter the first two terms : ");
		int a=s.nextInt();
		int b=s.nextInt();
		System.out.println("Enter the term you want : ");
		int n=s.nextInt();	
		System.out.println(n+"th term of fibonacci sequence is "+f.fibo(a,b,n));
		s.close();
	}
}
