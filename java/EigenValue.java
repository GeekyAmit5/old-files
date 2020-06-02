package algebra;

import java.util.*;

public class EigenValue {
	void display(double x[][])
	{
		System.out.println("The Matrix is : ");
		for(int i=0;i<x.length;i++)
		{
			for(int j=0;j<x.length;j++)
			{
				System.out.print(x[i][j]+"\t");
			}
			System.out.println();
		}
	}
	 double det(double A[][],int N)
	    {
	        double det=0;
	        if(N == 1)
	        {
	            det = A[0][0];
	        }
	        else if (N == 2)
	        {
	            det = A[0][0]*A[1][1] - A[1][0]*A[0][1];
	        }
	        else
	        {
	            det=0;
	            for(int j1=0;j1<N;j1++)
	            {
	                double[][] m = new double[N-1][];
	                for(int k=0;k<(N-1);k++)
	                {
	                    m[k] = new double[N-1];
	                }
	                for(int i=1;i<N;i++)
	                {
	                    int j2=0;
	                    for(int j=0;j<N;j++)
	                    {
	                        if(j == j1)
	                            continue;
	                        m[i-1][j2] = A[i][j];
	                        j2++;
	                    }
	                }
	                det += Math.pow(-1.0,1.0+j1+1.0)* A[0][j1] * det(m,N-1);
	            }
	        }
	        return det;
	    }
	 boolean check(double x[][],double e)
		{
		 for(int j=0;j<x.length;j++)
			{
				x[j][j]-=e;
			}
			 double c=det(x,x.length);
			 for(int j=0;j<x.length;j++)
				{
					x[j][j]+=e;
				}
				if(c==0)
					return true;
				else 
					return false;
		}
	 void hash(double x[][])
	 {
		 System.out.println("The Eigen Values are : ");
		 for(double i=-1000000;i<=1000000;i+=0.25)
		 {
			 if(check(x,i))
			 {
				 System.out.println(i);
			 }
		 }
	 }
	public static void main(String[] args) {
		EigenValue t=new EigenValue();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the Order of Square matrix : ");
		int n=s.nextInt();
		double x[][]=new double[n][n];
		System.out.println("Enter the elements Row-wise : ");
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				x[i][j]=s.nextDouble();
			}
		}
		t.display(x);
		t.hash(x);
		s.close();
	}
}
