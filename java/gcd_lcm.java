
import java.util.*;

public class gcd_lcm {
	/*
	 * int g(int x[])//recursive method { int n=x.length; int m[]=new int[n-1];
	 * while(n>1) { for(int i=0;i<n-1;i++) { m[i]=gcd(x[i],x[i+1]); } n--; for(int
	 * i=0;i<n;i++) { x[i]=m[i]; } } return m[0]; }
	 */
	int lcm(int x[]) {
		int i;
		for (i = max(x); i < 2147483647; i++) {
			if (check(x, i))
				break;
		}
		return i;
	}

	boolean check(int x[], int m) {
		for (int i = 0; i < x.length; i++)
			if (m % x[i] != 0)
				return false;
		return true;
	}

	int max(int x[]) {
		int m = x[0];
		for (int i = 0; i < x.length; i++) {
			if (x[i] > m) {
				m = x[i];
			}
		}
		return m;
	}

	int min(int x[]) {
		int m = x[0];
		for (int i = 0; i < x.length; i++) {
			if (x[i] < m) {
				m = x[i];
			}
		}
		return m;
	}

	int gcd(int x[]) {
		int i;
		for (i = min(x); i > 0; i--) {
			if (c(x, i))
				break;
		}
		return i;
	}

	boolean c(int x[], int m) {
		boolean t = true;
		for (int i = 0; i < x.length; i++) {
			if (x[i] % m != 0) {
				t = false;
				break;
			}
		}
		return t;
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		gcd_lcm g = new gcd_lcm();
		System.out.print("Enter the value for n : ");
		int x[] = new int[s.nextInt()];
		System.out.println("Enter Numbers ony by one : ");
		for (int i = 0; i < x.length; i++) {
			x[i] = s.nextInt();
		}
		System.out.println("GCD = " + g.gcd(x));
		System.out.println("LCM = " + g.lcm(x));
		s.close();
	}
}
