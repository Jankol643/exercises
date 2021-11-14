package chapter7;

public class A13_NegativeValsIterator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

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

}
