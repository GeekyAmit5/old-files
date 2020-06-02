package algebra;
import java.util.Scanner;
public class prime_between {
		private static Scanner s;
		int i,j,p=0;
		void prime(int m,int n)
		{
				System.out.println("Prime numbers from "+m+" to "+n+" are");
				for(i=m;i<=n;i++)
				{
					for(j=2;j<=i;j++)
					{
						if(i%j==0)
							break;
					}
					if(i==j)
					{
						System.out.println(i);
						p++;
					}	
				}
				System.out.println("Total : "+p);
		}
		public static void main(String args[])
		{
			prime_between p=new prime_between();
			s=new Scanner(System.in);
			System.out.print("Enter the lower bound : ");
			int m=s.nextInt();
			System.out.print("Enter the upper  bound : ");
			int n=s.nextInt();
			p.prime(m,n);
		}
}
