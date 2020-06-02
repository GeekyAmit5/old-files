package algebra;
import java.util.Scanner;

public class gcd {
	int g(int x,int y)
	{
		x=Math.abs(x);
		y=Math.abs(y);
		int r;
		while(y>0)
		{
			r=x%y;
			x=y;
			y=r;
		}
	return x;
	}
		int l(int x,int y)
		{
			int lcm=(x*y)/g(x,y);
			return lcm;
		}
	public static void main(String args[]) 
	{
		Scanner s=new Scanner(System.in);
		gcd g=new gcd();
		System.out.println("Enter the numbers : ");
		int a=s.nextInt();
		int b=s.nextInt();
		System.out.println("GCD of  "+a+" and "+b+" is "+ g.g(a,b));
		System.out.println("LCM of  "+a+" and "+b+" is "+ g.l(a,b));
		s.close();
	}
}
