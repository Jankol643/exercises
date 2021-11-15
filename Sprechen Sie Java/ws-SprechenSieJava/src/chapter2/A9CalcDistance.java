package chapter2;

import java.util.Scanner;

public class A9CalcDistance {

	public static void main(String[] args) {
		calcDistance();
	}
	
	public static void calcDistance() {
		System.out.print("Enter coordinates for the first point (format: x1 y1): ");
		Scanner scanner = new Scanner(System.in);
		String first = scanner.nextLine();
		System.out.print("Enter coordinates for the second point (format: x2 y2): ");
		String second = scanner.nextLine();
		scanner.close();
		
		String[] firstArr = first.split(" ");
		String[] secondArr = second.split(" ");
		int p1X = Integer.parseInt(firstArr[0]);
		int p1Y = Integer.parseInt(firstArr[1]);
		int p2X = Integer.parseInt(secondArr[0]);
		int p2Y = Integer.parseInt(secondArr[1]);
		
		int horizontalDistance = Math.abs(p2X - p1X);
		int verticalDistance = Math.abs(p2Y - p1Y);
		
		double distance = Math.sqrt(horizontalDistance * horizontalDistance + verticalDistance * verticalDistance);
		System.out.println("Distance: " + distance);
	}

}
