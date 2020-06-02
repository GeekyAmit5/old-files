
import java.util.*;

public class pythagorus {
		void  p(int n)
		{
			int c=0;
			System.out.println("The Pythgorean Triplets upto "+n+" are : ");
			for(int i=1;i<=n;i++)
			{
				for(int j=1;j<i;j++)
				{
					for(int k=1;k<j;k++)
					{
						if(i*i==j*j+k*k)
						{
							System.out.println(k+"   "+j+"   "+i);
							c++;
						}
					}
				}
			}
			System.out.println("Total : "+c);
		}
	    public static void main(String args[])
		    {		
		    	pythagorus p=new pythagorus();
		    	Scanner s =new Scanner(System.in);
		    	System.out.println("Enter the value of n : ");
		    	int n=s.nextInt();
		    	p.p(n);
		    	s.close();
		    }
	}
