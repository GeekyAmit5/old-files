package algebra;

import java.util.Scanner;

public class quadratic {
		void root(double x[])
		{
			double r1,r2;
			if(x[0]==0)
			{
				if(x[1]==0)
				{
					System.out.println("This equation can not have roots! ");
				}
				else
				{
					if(x[2]==0)
					{
						System.out.println("The roots is 0");
					}
					else
					{
						r1=-x[2]/x[1];
						System.out.println("Roots is "+r1);
					}
				}
			}
			else
			{
				double d=x[1]*x[1]-4*x[0]*x[2];
				if(d>=0)
				{
					r1=(-x[1]+Math.sqrt(d))/(2*x[0]);
					r2=(-x[1]-Math.sqrt(d))/(2*x[0]);
					System.out.println("Roots are : "+r1+"  And  "+r2);
				}
				else
				{
					double e=-d;
					double rer1=-x[1]/(2*x[0]);
					double imr1=Math.sqrt(e)/2;
					System.out.print("Roots are : "+rer1+" + "+imr1+"i   And  "+rer1+" - "+imr1+"i");
				}	
			}
		}
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		quadratic q=new quadratic();
		double x[]=new double[3];
		System.out.println("Enter the values of a , b and c : ");
		for(int i=0;i<3;i++)
		{
			x[i]=s.nextDouble();
		}
		q.root(x);
		s.close();
	}
}
