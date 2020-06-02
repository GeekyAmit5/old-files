package test;

public class prime_upto_infinity {
		int i=2,j,a=1;
		void prime()
		{
				while(a>0)
				{
					for(j=2;j<=i;j++)
					{
						if(i%j==0)
							break;
					}
					if(i==j)
					{
						System.out.println(i);
					}
					i++;
				}
		}
		    public static void main(String args[])
		    {		
		    	prime_upto_infinity p = new prime_upto_infinity();
		    	p.prime();
		    }
}

