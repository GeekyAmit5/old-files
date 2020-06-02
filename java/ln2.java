package test;

public class ln2 {
	double sum=0;
	 double sub=0;
	 int n=214748364;
	 double x()
	 {
		 	for(int i=1;i<=n;i+=2)
		 	{
		 			sum+=1/(double)i;
		 	}
		 	return sum;
	 }
		double y()
		{
			for(int i=2;i<=n;i+=2)
		 	{
		 			sub+=1/(double)i;
		 	}
		 	return sub;
		}
	public static void main(String[] args)
	{
			ln2 a=new ln2();
			System.out.println("ln(2) = "+(a.x()-a.y()));
	}
}
