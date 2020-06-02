package test;

import java.util.*;

public class Date {
		boolean isLeap(int y) 
		{
			if(y%4==0&&y%100!=0||y%400==0)
				return true;
			else 
				return false;
		}	
		public static void main(String args[])
		{
			Scanner s=new Scanner(System.in);
			Date date=new Date();
			System.out.println("Enter the date , month and Year : ");
			int d=s.nextInt();
			int m=s.nextInt();
			int y=s.nextInt();
			System.out.println("The Date is : "+d+"-"+m+"-"+y);
			if(date.isLeap(y))
			{
				System.out.println("The Year is Leap Year");
			}
			else
				System.out.println("The Year is NOT Leap Year");
			s.close();
		}
}
