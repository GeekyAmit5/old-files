import java.util.Random;

public class dice {
	public static void main(String[] args) {
		Random r= new Random();
    	int a=r.nextInt(7);
    	if(a==0)
    	{
    		while(a==0)
    		{
    			a+=r.nextInt(7);
    		}
    		System.out.println(a);
    	}
    	else
    		System.out.println(a);
	}
}
