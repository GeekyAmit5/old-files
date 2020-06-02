package test;
import java.util.Scanner;
public class addition {
	private static Scanner s;
	 void add(int x[][],int y[][],int n,int m)
	 {
		 int z[][]=new int[n][m];
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 z[i][j]=x[i][j]+y[i][j];
			 }
		 }
		 System.out.println("The Matrix A is : ");
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 System.out.print(x[i][j]+"     ");
			 }
			 System.out.println();
		 }
		 System.out.println("The Matrix B is : ");
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 System.out.print(y[i][j]+"     ");
			 }
			 System.out.println();
		 }
		 System.out.println("The Addition Matrix is : ");
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 System.out.print(z[i][j]+"     ");
			 }
			 System.out.println();
		 }
	 }
	public static void main(String[] args) 
	{
		s=new Scanner(System.in);
		addition a= new addition();
		System.out.println("Enter the number of rows and columns : ");
		int n=s.nextInt();
		int m=s.nextInt();
		int x[][]=new int[n][m];
		int y[][]=new int[n][m];
		System.out.println("Enter the elements of first Matrix  row-wise : ");
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 x[i][j]=s.nextInt();
			 }
		 }
		 System.out.println("Enter the elements of second Matrix row-wise : ");
		 for(int i=0;i<n;i++)
		 {
			 for(int j=0;j<m;j++)
			 {
				 y[i][j]=s.nextInt();
			 }
		 }
		 a.add(x, y, n, m);
	}
}
