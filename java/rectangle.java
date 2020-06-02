package test;

public class rectangle{
	double sum=0;
	double n=100000000000000.0;
	double x()
	 {
		 	for(int i=1;i<=(int)n;i++)
		 	{
		 			sum+=1/(double)i;
		 	}
		 	return sum;
		}
}