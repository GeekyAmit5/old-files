import java.util.*;

public class AntiPrime {
	int dc(int x)
	{
		int c=0;
		for(int i=1;i<=Math.abs(x);i++)
		{
			if(x%i==0)
			c++;
		}
		return c;
	}
	void ap(int n)
	{
		System.out.println("The Highly Composite Numbers Are :");
		int m=0;
		for(int i=1;i<=n;i++)
		{
		    if(dc(i)>m)
		    {
		    	m=dc(i);
		    	System.out.println(i);
		    }
		 }
	}
	public static void main(String[] args)
	{
		AntiPrime t=new AntiPrime();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the Upper Bound : ");
		int n=s.nextInt();
		t.ap(n);
		s.close();
	}
}
