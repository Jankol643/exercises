package sprechenSieJava;

public class Chapter6 {

	public static void main(String[] args) {
		double ar = area(6.0, 4.2, 2.5);
		System.out.println("Area: " + ar);
		int a = binToDec(11111111);
		System.out.println("Decimal: " + a);
	}

	/**
	 * Calculates the cubic root of a float using the Newton approximation
	 * @param x float to calculate
	 * @return cubic root
	 */
	public static float root3(float x) {
		float sqrt = 0;
		return sqrt;
	}

	/**
	 * Calculates the area of a triangle with the given lengths using the Heron formula
	 */
	public static double area(double a, double b, double c) {
		double ar = 0;
		double s = (a + b + c) / 2;
		ar = Math.sqrt(s * (s - a) * (s - b) * (s - c));
		return ar;
	}

	/**
	 * Converts a binary number to a decimal number
	 * @param int bin binary number
	 * @return decimal number
	 * @throws IllegalArgumentException if input is not valid
	 */
	public static int binToDec(int bin) {
		String binS = Integer.toString(bin);
		if (binS.length() > 8 || bin < 0)
			throw new IllegalArgumentException();
		
		int decimalnumber = 0;
		int power = 0;
		while(bin > 0)
		{
			int temp = bin % 10; // last digit of number
			decimalnumber += temp * Math.pow(2, power);
			bin = bin / 10;
			power++;
		}
		return decimalnumber;
	}

}
