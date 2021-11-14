package chapter7;

public class A1_InvertArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

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

}
