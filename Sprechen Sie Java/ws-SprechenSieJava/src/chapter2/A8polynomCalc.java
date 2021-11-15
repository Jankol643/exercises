package chapter2;

import java.util.Scanner;

public class A8polynomCalc {
	
	public static void main(String[] args) {
		
	}
	
	/**
	 * Reads integers from user and calculates the result of the polynom y = a*x^3+b*x^2+c*x+d
	 */
	public static void calculatePolynom() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a space separated array of integers: ");
		String str = scanner.nextLine();
		scanner.close();
		String[] strArray = str.split(" ");		
		int[] intArray = new int[strArray.length];
		int i = 0;
		for (String token : strArray){
		    intArray[i++] = Integer.parseInt(token); 
		}
		int a = intArray[0];
		int b = intArray[1];
		int c = intArray[2];
		int d = intArray[3];
		int x = intArray[4];
		
		double y = a * Math.pow(x, 3) + b * Math.pow(x, 2) + c * x + d;
		System.out.println(y + " = " + a + "*x^3 + " + b + "*x^2 + " + c + "*x + " + d);
	}
}
