package chapter4;

import java.util.Scanner;

public class A2NumberDigits {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Calculates the number of digits of a positive integer
	 * 
	 * @return number of digits
	 */
	public static int noDigits() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Please enter a positive integer: ");
		int n = sc.nextInt();
		sc.close();

		if (n >= 0) { // positive integer
			int digits = 1;
			int rem = n;
			while (rem > 10) {
				rem = (int) (rem / 10);
				digits += 1;
			}
			return digits;

		} else { // negative integer
			throw new ArithmeticException("Number has to be a positive integer");
		}
	}

}
