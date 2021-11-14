package chapter4;

import java.util.Scanner;

public class A3_DigitSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Reads an integer and calculates the digit sum
	 * 
	 * @return digit sum of positive integer
	 */
	public static int digitSum() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Please enter a positive integer: ");
		int n = sc.nextInt();
		sc.close();

		if (n >= 0) {
			int digitSum = 0;
			while (n > 0) {
				digitSum = digitSum + n % 10;
				n = n / 10;
			}
			return digitSum;
		} else { // negative integer
			throw new ArithmeticException("Number has to be a positive integer");
		}
	}

}
