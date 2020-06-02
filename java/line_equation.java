package test;

import java.util.*;

public class line_equation {
	double slope(int x[])
	{
		double s=(x[3]-x[1])/(double)(x[2]-x[0]);
		return s;
	}
	void equation(int x[])
	{
		int z[]=new int[3];
		z[1]=x[1]-x[3];
		z[2]=x[2]-x[0];
		z[0]=((x[0]*(x[1]-x[3]))-(x[1]*(x[0]-x[2])));
		System.out.println("Y-intercept  is : "+z[0]/(double)z[2]);
		System.out.println("X-intercept  is : "+z[0]/(double)z[1]);
		System.out.println("The Equation of the line is : "+z[1]+"x + "+z[2]+"y = "+z[0]);
	}
	public static void main(String[] args) 
	{
		line_equation l=new line_equation();
		Scanner s=new Scanner(System.in);
		System.out.println("Enter the points : ");
		int x[]=new int[4];
		for(int i=0;i<4;i++)
		{
			x[i]=s.nextInt();
		}
		System.out.println("Slope is : "+l.slope(x));
		l.equation(x);
		s.close();
	}
}
