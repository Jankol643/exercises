package sprechenSieJava;

/**
 * "Sprechen Sie Java" (Hanspeter Moessenboeck) - 4th edition
 * Chapter 3 - Verzweigungen
 * Created: 10/10/2021
 * @author Jankol643
 *
 */
public class Chapter3 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		// Verzweigungen();
		// Dreiecksbestimmung();
		//sort();
		//printCheckDate();
		//printWeekday();
		//checkOverflow();
	}

	/**
	 * Bestimmt, ob alle drei Werte verschieden oder mindestens zwei Werte gleich sind
	 */
	public static void Verzweigungen() {
		// TODO: Read values from user
		int x = 2;
		int y = 1;
		int z = 0;

		if (x != y) {
			if (x != z) {
				if (y != z) {
					System.out.println("Alle drei Werte verschieden.");
				}
			}
		}

		String msg = "Mindestens zwei Werte gleich";
		if ((x == y) || (y == z) || (x == z)) {
			System.out.println(msg);
		}
	}

	/**
	 * printlns the lateral length of a triangle and its type
	 */
	public static void Dreiecksbestimmung() {
		int x = 5;
		int y = 2;
		int z = 3;

		String triangleType = checkTriangleType(x, y, z);
		System.out.println("x: " + x + ", y: " + y + ", z: " + z+ ". ");
		System.out.println("Das Dreieck ist " + triangleType);
	}

	/**
	 * Checks if a triangle is equilateral (gleichseitig), right-angled, isosceles (gleichschenkelig), valid oder invalid
	 * @param x Seitenlaenge x des Dreiecks
	 * @param y Seitenlaenge y des Dreiecks
	 * @param z Seitenlaenge z des Dreiecks
	 * @return Art des Dreiecks
	 */
	public static String checkTriangleType(int x, int y, int z) {
		boolean checkPythagoras = checkPythagoras(x, y, z);
		if (x == y) {
			if (y == z) {
				return triangleType = "equilateral";
			}
			if (checkPythagoras) {
				return triangleType = "rightangled und isosceles";
			}
			return triangleType = "isosceles";
		}

		if (checkPythagoras) {
			return triangleType = "rightangled";
		}
		if (((x + y) <= z) || ((y + z) <= x) || ((x + z) <= y)) {
			return triangleType = "invalid";
		}
		return triangleType = "valid";

	}

	/**
	 * Pr�ft, ob drei Zahlen den Satz des Pythagoras erf�llen oder nicht
	 * @param x erste Zahl
	 * @param y zweite Zahl
	 * @param z dritte Zahl
	 * @return Satz des Pythagoras erf�llt oder nicht
	 */
	public static Boolean checkPythagoras(int x, int y, int z) {
		double dx = (double)(x);
		double dy = (double)(y);
		double dz = (double)(z);
		double two = (double)(2);
		if (Math.pow(dx, two) + Math.pow(dy, two) == Math.pow(dz, two)) {
			return true;
		}
		if (Math.pow(dy, two) + Math.pow(dz, two) == Math.pow(dx, two)) {
			return true;
		}
		if (Math.pow(dz, two) + Math.pow(dy, two) == Math.pow(dx, two)) {
			return true;
		}
		return false;
	}

	/**
	 * Reads three numbers and prints them sorted by value
	 * @param x Zahl 1
	 * @param y Zahl 2
	 * @param z Zahl 3
	 */
	public static void sort() {
		int x = 1;
		int y = -2;
		int z = 5;

		if (x < y) {
			assert (x < y);
			if (y < z) {
				assert (x < y) && (y < z);
				System.out.println(x + ", " + y + ", " + z);
				System.exit(0);
			}
			if (y > z) {
				assert (x < y) && (y > z);
				if (x < z) {
					assert (x < y) && (y > z) && (x < z);
					System.out.println(x + ", " + z + ", " + y);
					System.exit(0);					
				}
				if (x > z) {
					assert (x < y) && (y > z) && (x > z);
					System.out.println(z + ", " + x + ", " + y);						
				}
			}
		}
		else if (x > y) {
			assert (x > y);
			if (y < z) {
				assert (y < z);
				if (x < z) {
					assert (x > y) && (y < z) && (x < z);
					System.out.println(y + ", " + x + ", " + z);
				}
				if (x > z) {
					assert (x > y) && (y < z) && (x > z);
					System.out.println(y + ", " + z + ", " + x);
				}
				if (x == z) {
					assert (x > y) && (y < z) && (x == z);
					System.out.println(y + ", " + x + ", " + z);
				}
			}
			if (y > z) {
				assert (x > y) && (y > z);
				System.out.println(z + ", " + y + ", " + x);
			}
			if (y == z) {
				assert (x > y) && (y == z) && (x > z);
				System.out.println(y + ", " + z + ", " + x);
			}
		}
		else {
			assert (x == y);
			if (x < z) {
				assert (x == y) && (x < z);
				System.out.println(x + ", " + y + ", " + z);
			}
			if (x > z) {
				assert (x == y) && (x > z) && (y > z);
				System.out.println(z + ", " + x + ", " + y);
			}
			if (x == z) {
				assert (x == y) && (x == z);
				System.out.println(x + ", " + y + ", " + z);
			}
		}
	}

	/**
	 * prints the result of the date check
	 */
	public static void printCheckDate() {
		int day = 29;
		int month = 2;
		int year = 2017;
		
		boolean result = checkValidDate(day, month, year);
		System.out.println(day + ". " + month + ". " + year);
		System.out.println(": " + result);
	}

	/**
	 * Checks if a day is valid or not
	 * @param day
	 * @param month
	 * @param year
	 * @return valid or invalid
	 */
	public static boolean checkValidDate(int day, int month, int year) {
		// Input not valid
		if ((day <= 0) || (day > 31) || (month < 1) || (month > 12)) {
			return false;
		}
		
		if (year % 4 == 0) { // leap year
			if (month == 2) {
				if (day == 29) {
					return true;
				}
			}
		}
		if (year % 4 != 0) { // no leap year
			if (month == 2) {
				if (day == 29) {
					return false;
				}
			}
		}
		
		if (month % 2 == 1) { // uneven or odd month
			if (day == 31)
				return true;
			if (day == 30)
				return false;
			return true;
		}
		if (month % 2 == 0) { // even month
			if (day == 30)
				return true;
			if (day == 31)
				return false;
			return true;
		}
		return false;
	}
	
	/**
	 * prints the result of the weekday calculation
	 */
	public static void printWeekday() {
		int day = 29;
		int month = 2;
		int year = 2017;
		int firstJanuary = 4;
		
		String result = getWeekday(day, month, year, firstJanuary);
		System.out.println(day + ". " + month + ". " + year + "; ");
		System.out.print("Weekday of first January: " + firstJanuary);
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
		
		return weekday;
	}
	
	/**
	 * Checks if an overflow occurs when adding two numbers
	 */
	public static void checkOverflow() {
		int a = 2;
		int b = 5;
		
		if ((a + b) > Math.pow(2, 31) - 1 || (a + b) < Math.pow(-2, 31)) {
			System.out.println("a + b: overflow");
		}
		else
			System.out.println("a + b: no overflow");
	}
	
	public static void intersectLines() {
		int ax1 = 8; // line 1: (ax1, ay1), (ax2, ay2)
		int ay1 = 5;
		int ax2 = 5;
		int ay2 = 5;
		
		int bx1 = 8; // line 2: (bx1, by1), (bx2, by2)
		int by1 = 5;
		int bx2 = 5;
		int by2 = 5;
		
		// check if lines are horizontal or vertical
		if ((ay1 != ay2) || (ax1 != ax2)) {
			System.out.print("a must be horizontal or vertical");
			System.exit(-1);
		}
		if ((by1 != by2) || (bx1 != bx2)) {
			System.out.print("b must be horizontal or vertical");
			System.exit(-1);
		}
		
		
	}
	
}