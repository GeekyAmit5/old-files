package algebra;

import java.util.*;

public class relatively_prime {
	int gcd(int x,int y)
	{
		int r;
		while(y>0)
		{
			r=x%y;
			x=y;
			y=r;
		}
		return x;
	}
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		relatively_prime r= new relatively_prime();
		System.out.print("Enter the number : ");
		int n=s.nextInt();
		System.out.println("The numbers that are relatively prime to "+n+" are : ");
		int c=0;
		for(int i=1;i<=n;i++)
		{
			if(r.gcd(n,i)==1)
			{
				System.out.println(i);
				c++;
			}
		}
		System.out.print("Total : "+c);
		s.close();
	}
}
