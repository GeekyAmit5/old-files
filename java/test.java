
import java.util.*;

public class test {
	int dc(double x)
	{
		int c=1;
		for(int i=1;i<Math.abs(x);i++)
		{
			if(x%i==0)
			{
				c++;
			}
		}
		return c;
	}
	int[] divList(int x)
	{
		int l[]=new int[dc(x)];
		int j =0;
		for(int i=1;i<=x;i++)
		{
			if(x%i==0)
			{
				l[j]=i;
				j++;
			}
		}
		return l;
	}
	public static void main(String[] args) 
	{
		test t=new test();
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the Number : ");
		int n=s.nextInt();
		for(int i=0;i<t.divList(n).length;i++)
		{
			System.out.println(t.divList(n)[i]);
		}
		s.close();
	}
}
