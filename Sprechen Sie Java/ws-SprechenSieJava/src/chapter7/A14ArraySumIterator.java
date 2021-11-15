package chapter7;

public class A14ArraySumIterator {

	public static void main(String[] args) {

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

}
