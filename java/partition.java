
import java.util.*;

public class partition {
	int S(int n, int k) {
		if (k == 0)
			return 0;
		else if (n == k || k == 1)
			return 1;
		else
			return S(n - 1, k - 1) + k * S(n - 1, k);
	}

	public static void main(String[] args) {
		partition p = new partition();
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the value of n and k : ");
		int n = s.nextInt();
		int k = s.nextInt();
		if (k > n)
			System.out.println("k must be smaller than or equal to n");
		else
			System.out.println("S(" + n + "," + k + ") = " + p.S(n, k));
		s.close();
	}
}
