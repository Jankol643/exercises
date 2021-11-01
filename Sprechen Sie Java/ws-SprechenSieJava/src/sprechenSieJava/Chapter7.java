package sprechenSieJava;

import java.util.Scanner;
import java.util.Arrays;

public class Chapter7 {

	public static void main(String[] args) {
		printInverted();
	}
	
	/**
	 * Gets the main Java version
	 * @return
	 */
	private static int getVersion() {
		String version = System.getProperty("java.version");
		if(version.startsWith("1.")) {
			version = version.substring(2, 3);
		} else {
			int dot = version.indexOf(".");
			if(dot != -1) { version = version.substring(0, dot); }
		} return Integer.parseInt(version);
	}

	/**
	 * Calls functions to read and invert an integer array
	 */
	public static void printInverted() {
		int[] arr = inputArray();
		int[] inverted = invert(arr);
		System.out.println(Arrays.toString(inverted));
	}
	
	/**
	 * Returns an integer array from space separated user input
	 * @return length of integer array, integer array
	 */
	public static int[] inputArray() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a space separated array of integers: ");
		String str = scanner.nextLine();
		scanner.close();
		String[] strArray = str.split(" ");
		int[] intArray = new int[strArray.length];

		int i = 0;
		for (String token : strArray){
		    intArray[i++] = Integer.parseInt(token); 
		}
		return intArray;
	}
	
	/**
	 * Inverts a given integer array
	 * @param a array of int
	 * @return inverted array
	 */
	public static int[] invert(int[] a) {
		int length = a.length;
		int[] arr = new int[length];
		for (int i = 0; i < length; i++) {
			arr[i] = a[length - 1 - i];
		}
		return arr;
	}
	
	public static void matrixManipulation() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a positive whole number: ");
		int n = scanner.nextInt();
		scanner.close();
		int[][] arr = readArray(n);
		if (checkMatrixSymmetry(arr) == true)
			transformMatrix(arr);
	}

	public static int[][] readArray(int n) {
		int[][] tmp = new int[n];
		for (int i = 0; i <= n; i++) {
			tmp[i] = inputArray();
		}
		int[][] arr = new int[n][n];
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++) {
				arr[i][j] = tmp[i][j];
			}
		}
		return arr;
		// array into form int[][]
	}
	
	public static boolean checkMatrixSymmetry(int[][] matrix) {
		boolean symmetrical = false;

		return symmetrical;
	}

	public static int[][] transformMatrix(int[][] matrix) {
		int[][] result;
		return result;
	}

	/**
	 * Counts the number of negative values in an array
	 * @param a integer array
	 * @return number of negative values
	 */
	public static int negativeValues(int[] a) {
		int count = 0;
		for(int number: a) {
			if (number < 0)
				count = count + 1;
		}
		return count;
	}

	/**
	 * Returns the sum of all values in a two-dimensional array
	 * Requires Java >= 5
	 * @param a integer array consisting of integer arrays
	 * @return sum of integers
	 */
	public static int sum(int[][] a) {
		int sum = 0;
		for(int[] line : a) {
			for(int i : line)
				sum += i;
		}
		return sum;
	}

	/**
	 * Calculates the maximum of an arbitrary length of parameters
	 * Requires Java >= 5
	 * @param values list of parameters
	 * @return maximum
	 */
	public static int maxVariableInt(int... values) {
		int max = values[0];
		for(int n: values) {
			if (n > max)
				max = n;
		}
		return max;
	}

	/**
	 * Calculates the value of a polynom with an arbitrary length of parameters
	 * @param params
	 * @return
	 */
	public static double poly(int x, int... params) {
		double y = 0;
		int count = params.length;
		for(int i = 0; i < params.length; i++) {
			int par = params[i];
			y = y + par * Math.pow(x, count - i);
		}
		return y;
	}

}
