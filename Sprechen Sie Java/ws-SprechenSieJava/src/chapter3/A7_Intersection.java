package chapter3;

import java.util.Scanner;

public class A7_Intersection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Calculates the intersections of two lines
	 */
	public static void intersectLines() {
		System.out.print("Enter coordinates for the first line (format: ax1 ay1 ax2 ay2 ): ");
		Scanner scanner = new Scanner(System.in);
		String first = scanner.nextLine();
		System.out.print("Enter coordinates for the second line (format: bx1 by1 bx2 by2 ): ");
		String second = scanner.nextLine();
		scanner.close();
		
		String[] firstArr = first.split(" ");
		String[] secondArr = second.split(" ");
		
		// line 1: (ax1, ay1), (ax2, ay2)
		int ax1 = Integer.parseInt(firstArr[0]);
		int ay1 = Integer.parseInt(firstArr[1]);
		int ax2 = Integer.parseInt(firstArr[2]);
		int ay2 = Integer.parseInt(firstArr[3]);
		
		 // line 2: (bx1, by1), (bx2, by2)
		int bx1 = Integer.parseInt(secondArr[0]);
		int by1 = Integer.parseInt(secondArr[1]);
		int bx2 = Integer.parseInt(secondArr[2]);
		int by2 = Integer.parseInt(secondArr[3]);

		// check if lines are horizontal or vertical
		if ((ay1 != ay2) || (ax1 != ax2)) {
			System.out.println("a must be horizontal or vertical");
			System.exit(-1);
		}
		if ((by1 != by2) || (bx1 != bx2)) {
			System.out.println("b must be horizontal or vertical");
			System.exit(-1);
		}


	}

}
