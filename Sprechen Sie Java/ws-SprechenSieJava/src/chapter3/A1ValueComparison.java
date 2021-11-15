package chapter3;

import java.util.Scanner;

public class A1ValueComparison {

	public static void main(String[] args) {
		valueComps();
	}

	/**
	 * Checks if all three input values are different or if at least two values are equal
	 */
	public static void valueComps() {
		System.out.print("Enter three space separated numbers: ");
		Scanner scanner = new Scanner(System.in);
		String first = scanner.nextLine();
		scanner.close();

		String[] strArr = first.split(" ");
		int x = Integer.parseInt(strArr[0]);
		int y = Integer.parseInt(strArr[1]);
		int z = Integer.parseInt(strArr[2]);

		boolean threeDifferent = x != y && x!= z && y != z;
		if (threeDifferent) {
			System.out.println("All three values different.");
		}

		boolean twoEqual = (x == y) || (y == z) || (x == z);
		if (twoEqual) {
			System.out.println("At least two equal values");
		}

	}
}
