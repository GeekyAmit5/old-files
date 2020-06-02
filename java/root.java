import java.util.*;

public class root {
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
	void r(double a[])
	{
		int j1=0,j2=0;
    	 int x[]=new int[dc(a[a.length-1])];
    	 for(int i=1;i<=Math.abs(a[a.length-1]);i++)
    	 {
    		 if(a[a.length-1]%i==0)
    		 {
    			x[j1]=i;
    			j1++;
    		 }
    	 }
    	 int y[]=new int[dc(a[0])];
    	 for(int i=1;i<=Math.abs(a[0]);i++)
    	 {
    		 if(a[0]%i==0)
    		 {
    			y[j2]=i;
    			j2++;
    		 }
    	 }
    	 double x1[][]=new double[dc(a[a.length-1])][dc(a[0])];
    	 for(int i=0;i<dc(a[a.length-1]);i++)
    	 {
    		 for(int j=0;j<dc(a[0]);j++)
    		 {
    			 x1[i][j]=y[j]/(double)x[i];
    		 }
    	 }
    	 boolean t=false;
    	 for(int i=0;i<dc(a[a.length-1]);i++)
    	 {
    		 for(int j=0;j<dc(a[0]);j++)
    		 {
    			if(check(a,x1[i][j])||check(a,-x1[i][j]))
   				t=true;
    		 }
    	 }
    	 if(a.length==3||a.length==2)
    	 t=true;
    	 if(t) {
	System.out.println();
    	 System.out.println("The Roots are : ");
	if(a.length==2)
	{
		 System.out.println(-a[0]/a[1]);
	}
    	else if(a.length==3)
    	 {
    		 double d=a[1]*a[1]-4*a[2]*a[0];
		if(d>=0)
		{
			double r1=(-a[1]+Math.sqrt(d))/(2*a[2]);
			double r2=(-a[1]-Math.sqrt(d))/(2*a[2]);
			System.out.println(r2);
			System.out.println(r1);
		}
		else
		{
			double e=-d;
			double rer1=-a[1]/(2*a[2]);
			double imr1=Math.sqrt(e)/2;
			System.out.println(rer1+" + "+imr1+"i");
			System.out.println(rer1+" - "+imr1+"i");
		}	
    	 }
    	 else if(a[0]!=0) {
    	 for(int i=0;i<dc(a[a.length-1]);i++)
    	 {
    		 for(int j=0;j<dc(a[0]);j++)
    		 {
   			if(check(a,x1[i][j]))
   	   		{
   				System.out.println(x1[i][j]);
   	   		}
   	   		if(check(a,-x1[i][j]))
   		   	{
   	   			System.out.println(-x1[i][j]);
   		   	}
   		 }
   		}
    	}
    	 else
    	 {
    		 int n=100000;
    		 for(double i=-n;i<=n;i+=0.25)
    		 {
    			 if(check(a,i))
    			 {
    				 System.out.println(i);
    			 }
    		 }
    	 }
    }
    else
    System.out.println("This Polynomial have NO Rational Roots !");
	}
	boolean check(double x[],double r)
	{
		double s=0;
		for(int i=0;i<x.length;i++)
		{
			s+=x[i]*Math.pow(r,i);
		}
		if(s==0)
			return true;
		else 
			return false;
	}
	void display(double a[])
	{
		System.out.println();
		System.out.println("The Polynomial is : ");
		System.out.print(a[0]);
		for(int i=1;i<a.length;i++)
		{
			System.out.print(" + "+a[i]+"x^"+i);
		}
		System.out.println();
	}
	public static void main(String[] args) 
	{
		root r=new root();
		Scanner s=new Scanner(System.in);
		System.out.print("Enter the Degree of the Polynomial : ");
		double x[]=new double[s.nextInt()+1];
		System.out.print("Enter the Coefficients of the Polynomial : ");
		System.out.println("a0+a1x+a2x^2+....+anx^n=0");
		for(int i=0;i<x.length;i++)
		{
			x[i]=s.nextDouble();
		}
		if(x[x.length-1]==0)
		{
			System.out.print("The Degree of the Polynomial is "+(x.length-1)+" So Coefficient of a"+(x.length-1)+" Can't be Zero");
		}
		else
		{
			r.display(x);
			r.r(x);
			s.close();
		}
	}
}
