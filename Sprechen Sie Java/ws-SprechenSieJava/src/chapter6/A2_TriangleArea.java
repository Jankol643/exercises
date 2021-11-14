package chapter6;

public class A2_TriangleArea {

	public static void main(String[] args) {

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

}
