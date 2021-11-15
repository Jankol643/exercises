package chapter3;

import java.util.Scanner;

public class A3Sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Reads three numbers and prints them sorted by value
	 */
	public static void sort() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter three numbers separated by spaces: ");
		String input = s.nextLine();
		s.close();
		String[] splitted = input.split(" ");
		int x = Integer.valueOf(splitted[0]);
		int y = Integer.valueOf(splitted[1]);
		int z = Integer.valueOf(splitted[2]);

		if (x < y) {
			assert (x < y);
			if (y < z) {
				assert (x < y) && (y < z);
				System.out.println(x + ", " + y + ", " + z);
				System.exit(0);
			}
			if (y > z) {
				assert (x < y) && (y > z);
				if (x < z) {
					assert (x < y) && (y > z) && (x < z);
					System.out.println(x + ", " + z + ", " + y);
					System.exit(0);					
				}
				if (x > z) {
					assert (x < y) && (y > z) && (x > z);
					System.out.println(z + ", " + x + ", " + y);						
				}
			}
		}
		else if (x > y) {
			assert (x > y);
			if (y < z) {
				assert (y < z);
				if (x < z) {
					assert (x > y) && (y < z) && (x < z);
					System.out.println(y + ", " + x + ", " + z);
				}
				if (x > z) {
					assert (x > y) && (y < z) && (x > z);
					System.out.println(y + ", " + z + ", " + x);
				}
				if (x == z) {
					assert (x > y) && (y < z) && (x == z);
					System.out.println(y + ", " + x + ", " + z);
				}
			}
			if (y > z) {
				assert (x > y) && (y > z);
				System.out.println(z + ", " + y + ", " + x);
			}
			if (y == z) {
				assert (x > y) && (y == z) && (x > z);
				System.out.println(y + ", " + z + ", " + x);
			}
		}
		else {
			assert (x == y);
			if (x < z) {
				assert (x == y) && (x < z);
				System.out.println(x + ", " + y + ", " + z);
			}
			if (x > z) {
				assert (x == y) && (x > z) && (y > z);
				System.out.println(z + ", " + x + ", " + y);
			}
			if (x == z) {
				assert (x == y) && (x == z);
				System.out.println(x + ", " + y + ", " + z);
			}
		}
	}


}
