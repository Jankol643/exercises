package chapter7;

public class A15MaxParams {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

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

}
