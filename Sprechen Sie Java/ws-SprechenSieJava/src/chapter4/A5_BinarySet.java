package chapter4;

import java.util.Scanner;

public class A5_BinarySet {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	

	/**
	 * Reads a binary number and returns which bits are 1
	 * 
	 * @return string with digit positions
	 */
	public static String setOfBinary() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Please enter a positive binary number: ");
		int n = sc.nextInt();
		sc.close();

		if (n >= 0) {
			int pos = 0;
			int digit;
			String str = "";
			while (n > 0) {

				digit = n % 10;
				if (digit == 1) {
					if (str.isEmpty())
						str = str + pos;
					else
						str = str + ", " + pos;
				}
				n = n / 10;
				pos++;
			}
			return str;
		} else { // negative integer
			throw new ArithmeticException("Number has to be a positive binary number");
		}
	}

}
