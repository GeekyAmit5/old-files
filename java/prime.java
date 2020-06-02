
import java.util.Scanner;

public class prime { // to check if a numbers is prime or not
	boolean p(int x) {
		int i;
		for (i = 2; i <= x; i++) {
			if (x % i == 0)
				break;
		}
		return i == x;
	}

	public static void main(String args[]) {
		// prime a=new prime();
		Scanner s = new Scanner(System.in);
		System.out.print("Enter the number : ");
		int n = s.nextInt();
		int i;
		boolean p = true;
		for (i = 2; i < n; i++) {
			if (n % i == 0) {
				p = false;
				break;
			}
		}
		if (p) {
			if (n == 1) {
				System.out.println(n + " is not Prime");
			} else
				System.out.println(n + " is Prime");
		} else {
			System.out.println(n + " is not Prime");
			System.out.println("Because " + i + " divides " + n);
		}
		/*
		 * if(a.p(n)) //alternate method { System.out.println(n+" is Prime"); } else {
		 * System.out.println(n+" is not Prime"); }
		 */
		s.close();
	}
}
