package algebra;
import java.util.Scanner;
public class prime_upto_n {
		private static Scanner s;
		int i,j,p=0;
		void prime(int n)
		{
				System.out.println("Prime numbers from 1 to "+n+" are");
				for(i=2;i<=n;i++)
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
			prime_upto_n a=new prime_upto_n();
			s=new Scanner(System.in);
			System.out.print("Enter the value of n : ");
			int n=s.nextInt();
			a.prime(n);
		}
}
