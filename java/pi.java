package test;

public class pi {
	double s=0;
	double x=0;
	int  n=1000000000;
	double sum()
		{
			for(int i=1;i<=n;i+=4)
			{
				 s+=4/(double)i;
			}
			return s;
		}
	double sub()
		{
			for(int i=3;i<=n;i+=4)
			{
				 x+=4/(double)i;
			}
			return x;
		}
}
