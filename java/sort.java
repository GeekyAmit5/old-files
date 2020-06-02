
import java.util.Scanner;

public class sort {
	int t;
	static int n;
	int x[] = new int[n];

	void bubbleSort() {
		for (int i = 0; i < x.length; i++) {
			for (int j = i + 1; j < x.length; j++) {
				if (x[i] > x[j]) {
					t = x[i];
					x[i] = x[j];
					x[j] = t;
				}
			}
		}
		System.out.println("Ascending\tDecending : ");
		for (int i = 0; i < x.length; i++)
			System.out.println(x[i] + "\t\t" + x[x.length - 1 - i]);
	}

	public static void main(String args[]) {
		Scanner a = new Scanner(System.in);
		System.out.println("Enter the value of n : ");
		sort.n = a.nextInt();
		sort s = new sort();
		System.out.println("Enter elements one by one : ");
		for (int i = 0; i < sort.n; i++) {
			s.x[i] = a.nextInt();
		}
		s.bubbleSort();
		a.close();
	}
}
