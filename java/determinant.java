
import java.util.*;
 
public class determinant {
    public double det(double A[][],int N)
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
    void display(double a[][],int m)
    {
    	System.out.println("The Matrix is : ");
    	for(int i=0;i<m;i++)
    	{
    		for(int j=0;j<m;j++)
    		{
    			System.out.print(a[i][j]+"\t");
    		}
    		System.out.println();
    	}
    }
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the order of the square matrix : ");
        int n = s.nextInt();
        System.out.println("Enter the elements of the square matrix");
        double[][] x = new double[n][n];
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                x[i][j] = s.nextDouble();
            }
        }
        determinant d=new determinant();
        d.display(x,n);
        System.out.println("The determinant of the Matrix is : "+d.det(x, n));
        s.close();
    }
}