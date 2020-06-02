
import java.util.*;

public class distance {
	double d(int x[],int y[],int n)
	{
		int s=0;
		for(int i=0;i<n;i++)
		{
			s+=(x[i]-y[i])*(x[i]-y[i]);
		}
		return Math.sqrt(s);
	}
	public static void main(String[] args) {
		distance d=new distance();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter The Value of n : ");
		int n=s.nextInt();
		System.out.println("Enter Coordinates of The First Point");
		int x[]=new int[n];
		for(int i=0;i<n;i++)
		{
			x[i]=s.nextInt();
		}
		System.out.println("Enter Coordinates of The Second Point");
		int y[]=new int[n];
		for(int i=0;i<n;i++)
		{
			y[i]=s.nextInt();
		}
		System.out.println("Distance Between The Points is : "+d.d(x,y,n));
		s.close();
	}
}
