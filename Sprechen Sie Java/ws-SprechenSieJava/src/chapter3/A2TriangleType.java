package chapter3;

import java.util.Scanner;

public class A2TriangleType {

	public static void main(String[] args) {

	}
	
	/**
	 * Prints the lateral length of a triangle and its type
	 */
	public static void TriangleType() {
		System.out.print("Enter three space separated numbers: ");
		Scanner scanner = new Scanner(System.in);
		String first = scanner.nextLine();
		scanner.close();

		String[] strArr = first.split(" ");
		int x = Integer.parseInt(strArr[0]);
		int y = Integer.parseInt(strArr[1]);
		int z = Integer.parseInt(strArr[2]);

		String triangleType = checkTriangleType(x, y, z);
		System.out.println("x: " + x + ", y: " + y + ", z: " + z+ ". ");
		System.out.println("The triangle is: " + triangleType);
	}

	/**
	 * Checks if a triangle is equilateral (gleichseitig), right-angled, isosceles (gleichschenkelig), valid oder invalid
	 * @param x length of side x
	 * @param y length of side y
	 * @param z length of side z
	 * @return type of triangle
	 */
	public static String checkTriangleType(int x, int y, int z) {
		boolean checkPythagoras = checkPythagoras(x, y, z);
		String triangleType = "";
		if (x == y) {
			if (y == z) {
				triangleType = "equilateral";
				return triangleType;				
			}
			if (checkPythagoras) {
				triangleType = "rightangled und isosceles";
				return triangleType;
			}
			triangleType = "isosceles";
			return triangleType;
		}
		
		if (checkPythagoras) {
			triangleType = "rightangled";
			return triangleType;			
		}

		boolean invalid = ((x + y) <= z) || ((y + z) <= x) || ((x + z) <= y);
		if (invalid) {
			triangleType = "invalid";
			return triangleType;			
		}

		if (triangleType.isEmpty())
			triangleType = "valid";
			return triangleType;
	}

	/**
	 * Tests whether three numbers fulfill the pythagorean theorem
	 * @param x first digit
	 * @param y second digit
	 * @param z third digit
	 * @return true or false
	 */
	public static boolean checkPythagoras(int x, int y, int z) {
		double dx = (double)(x);
		double dy = (double)(y);
		double dz = (double)(z);
		boolean fulfilled1 = dx * dx + dy * dy == dz * dz;
		boolean fulfilled2 = dy * dy + dz * dz == dx * dx; 
		boolean fulfilled3 = dz * dz + dy * dy == dx * dx; 
		if (fulfilled1 || fulfilled2 || fulfilled3)
			return true;
		return false;
	}

}
