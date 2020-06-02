import java.util.*;

public class BE {
	int fact(int x)
	{
		if(x<=1)
			return 1;
		else
			return x*fact(x-1);			
	}
	int nCr(int n,int r)
	{
		return fact(n)/(fact(r)*fact(n-r));
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
		BE e=new BE();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the value of n : ");
		e.exp(s.nextInt());
		s.close();
	}
}