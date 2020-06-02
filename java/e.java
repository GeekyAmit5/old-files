package test;

public class e {
	 double s=0;
	 double sum(int n)//using series
	 {
		 	for(int i=0;i<=n;i++)
		 	{
		 			s+=1/fact(i);
		 	}
		 	return s;
	 }
		double fact(int x)
		{
			if(x<=1)
				return 1;
			else 
				return x*fact(x-1);
		}
		double alternate()//using limit formula
		{
			double e=Math.pow((1+1/2147483647.0), 2147483647);
			return e;
		}
		public static void main(String args[])
		{
			e a=new e();
			System.out.println("e = "+a.sum(10000));
			System.out.println("e = " +a.alternate());
		}
}
