package chapter3;

import java.util.Scanner;

public class A4_ValidDateCheck {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	

	/**
	 * prints the result of the date check
	 */
	public static void printCheckDate() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter three numbers separated by spaces: ");
		String input = s.nextLine();
		s.close();
		String[] splitted = input.split(" ");
		int day = Integer.valueOf(splitted[0]);
		int month = Integer.valueOf(splitted[1]);
		int year = Integer.valueOf(splitted[2]);

		boolean result = checkValidDate(day, month, year);
		System.out.print(day + ". " + month + ". " + year);
		System.out.print(": " + result);
	}

	/**
	 * Checks if a date is valid or not
	 * @param day
	 * @param month
	 * @param year
	 * @return valid or invalid
	 */
	public static boolean checkValidDate(int day, int month, int year) {
		// Input not valid
		if ((day <= 0) || (day > 31) || (month < 1) || (month > 12) || (year < 0))
			return false;

		if (year % 4 == 0 && month == 2 && day == 29) // leap year
			return true;

		if (year % 4 != 0 && month == 2 && day == 29) // no leap year
			return false;

		if (month % 2 == 1) { // uneven or odd month
			if (day == 30)
				return false;
			return true;
		}
		if (month % 2 == 0) { // even month
			if (day == 31)
				return false;
			return true;
		}
		return false;
	}


}
