package chapter3;

public class A6Overflow {
	public static void main(String[] args) {
		
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
}
