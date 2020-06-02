package test;

public class goldenratio {
	double gr()
	{
		int a=1,b=1,c;
		for(int i=0;i<44;i++)
		{
			c=a+b;
			a=b;
			b=c;
		}
		return (b/(double)a);
	}
	public static void main(String args[]) {
	goldenratio g=new goldenratio();
	System.out.println(" The Golden Ratio is "+g.gr());
	}
}
