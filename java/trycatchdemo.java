
public class trycatchdemo {
	public static void main(String args[]) {
		int i = 10, b = 0, a;
		try {
			a = i / b;
		} catch (ArithmeticException e) {
			System.out.println("Error has found " + e);
		} finally {
			System.out.println(b);
		}
	}
}
