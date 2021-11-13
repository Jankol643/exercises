package sprechenSieJava;

import java.util.Scanner; // Import the Scanner class to read input
import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors

public class Chapter4 {

	public static void main(String[] args) {
		// int digits = noDigits();
		// System.out.println("Number of digits: " + digits);
		// int digitSum = digitSum();
		// System.out.println("Digit sum: " + digitSum);
		// String set = setOfBinary();
		// System.out.println(set);
		numberStatistics();
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

	/**
	 * Prints the minimum, maximum and average from a line of numbers read from a
	 * file
	 */
	public static void numberStatistics() {
		// read first line of file
		String filename = "4_numberStatistics.txt";
		filename = "resources/" + filename;
		String data = "";
		try {
			File myObj = new File(filename);
			Scanner myReader = new Scanner(myObj);
			data = myReader.nextLine();
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("File could not be found.");
			e.printStackTrace();
		}

		// assuming that data is a space separated string of integers
		String[] strArray = data.split(" ");
		System.out.println(data);
		int[] intArray = new int[strArray.length];
		int i = 0;
		for (String token : strArray) {
			intArray[i++] = Integer.parseInt(token);
		}

		int max = 0;
		int min = 0;
		int sum = 0;
		int count = intArray.length;

		for (int number : intArray) {
			if (number < min)
				min = number;
			else if (number > max) {
				max = number;
			}
			sum += number;
		}

		float avg = sum / count;
		System.out.println("minimum: " + min);
		System.out.println("maximum: " + max);
		System.out.println("average: " + avg);
	}

	/**
      * Calculates the prime factors that make up the number n.
      * If you multiply them, you get the number.
      * The numbers are returned in an array that has so many elements
      * as n has prime factors. They are sorted in ascending order.
      *
      * @param n The number to be partitioned
      * @return The prime factors in an array
      * 
	 */
	public static long[] primeFactorization() {
		/**
		 * The procedure is as follows:
         * Due to the requirement that the returned array is a maximum it
         * may have as many elements as the number n has prime factors,
         * we first create a "temporary" array tmp, whose
         * length is given by maxFactors. This happens from
         * a consideration of memory usage:
         * You could also initialize tmp with the length n, however
         * this is rather suboptimal from an efficiency point of view,
         * since each number has a maximum of a certain number of prime factors.
         * Since 2 is the smallest possible prime factor, the number is the
         * Prime factors always less than or equal to the exponent of the next
         * higher power of two.
         * It follows:
         * n <= 2 ^ x
         * log (n) <= log (2 ^ x)
         * x> = log (n) / log (2)
         * With x as the maximum number of prime factors of the number n.
		 */

        // Determine the maximum number of factors
        int maxFactors = (int) Math.ceil (Math.log10 (n) / Math.log10 (2));

		int countPrimefactors = 0;
		long[] tmp = new long[maxFactors];

		for (long j = 2; j <= n; j++) {
			if (n % j == 0) { // Is j a primefactor?
				tmp[countPrimefactors++] = j; // save primefactor
				n = n / j;
				j = 1; // reset j to start value 2 (1++)
			}
		}

		// Generate return array with the length of the actual number of prime factors
		long[] prf = new long[countPrimefactors];
		// Transfer the values of the temporary array into the return array
		for (int i = 0; i < countPrimefactors; i++) {
			prf[i] = tmp[i];
		}
		return prf;
	}

}
