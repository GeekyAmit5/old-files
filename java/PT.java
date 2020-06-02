
import java.util.*;

public class PT {
	int nCr(int n, int r) {
		if (r == 0 || r == n)
			return 1;
		else
			return nCr(n - 1, r - 1) + nCr(n - 1, r);
	}

	void pt(int n) {
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= i; j++) {
				System.out.print(nCr(i, j) + "\t");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		PT p = new PT();
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the number of rows : ");
		int n = s.nextInt();
		System.out.println("Pascals Triangle upto " + n + " rows is : ");
		p.pt(n);
		s.close();
	}
}
