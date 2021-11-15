package chapter3;

import java.util.Scanner;

public class A5CalcWeekday {

	public static void main(String[] args) {

	}
	
	/**
	 * prints the result of the weekday calculation
	 */
	public static void printWeekday() {
		System.out.print("Enter a date separated by spaces and the first day of the year: ");
		Scanner s = new Scanner(System.in);
		String input = s.nextLine();
		s.close();
		String[] splitted = input.split(" ");

		int day = Integer.parseInt(splitted[0]);
		int month = Integer.parseInt(splitted[1]);
		int year = Integer.parseInt(splitted[2]);
		int firstJanuary = Integer.parseInt(splitted[3]);

		String result = getWeekday(day, month, year, firstJanuary);
		System.out.println(day + ". " + month + ". " + year + "; ");
		System.out.println("Weekday of first January: " + firstJanuary);
		System.out.println("Weekday of date: " + result);
	}

	/**
	 * Returns the weekday of a given date as a string
	 * @param day
	 * @param month
	 * @param year
	 * @param firstJanuary weekday of first January of given year
	 * @return weekday
	 */
	public static String getWeekday(int day, int month, int year, int firstJanuary) {
		String weekday = "";
		String[] possibleWeekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
		int dayOfYear = firstJanuary + day - 1;
		switch (month) {
		case 1: break;
		case 2: dayOfYear += 31; break;
		case 3: dayOfYear += 59; break;
		case 4: dayOfYear += 90; break;
		case 5: dayOfYear += 120; break;
		case 6: dayOfYear += 151; break;
		case 7: dayOfYear += 181; break;
		case 8: dayOfYear += 212; break;
		case 9: dayOfYear += 243; break;
		case 10: dayOfYear += 273; break;
		case 11: dayOfYear += 304; break;
		case 12: dayOfYear += 334; break;
		}

		// check for leap years
		if (month > 2 && year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
			dayOfYear++;

		int w = dayOfYear % 7;
		switch (w) {
		case 1: weekday = possibleWeekdays[0]; break;
		case 2: weekday = possibleWeekdays[1]; break;
		case 3: weekday = possibleWeekdays[2]; break;
		case 4: weekday = possibleWeekdays[3]; break;
		case 5: weekday = possibleWeekdays[4]; break;
		case 6: weekday = possibleWeekdays[5]; break;
		case 7: weekday = possibleWeekdays[6]; break;
		}
		return weekday;
	}

}
