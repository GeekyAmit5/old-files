package algebra;
import java.util.Scanner;

public class divisor {
		int p=0;
		void div(int x)
		{
			System.out.println("Divisors of "+x+" are");
			for(int i=1;i<=x;i++)
			{
				if(x%i==0)
				{
					System.out.println(i);
					p++;
				}		
			}
			System.out.println("Total : "+p);
		}
		public static void main(String args[])
		{
			Scanner s=new Scanner(System.in);
			divisor d=new divisor();
			System.out.print("Enter the number : ");
			int x=s.nextInt();
			d.div(x);
			s.close();
		}
}
