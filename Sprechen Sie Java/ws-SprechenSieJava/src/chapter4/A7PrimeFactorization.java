package chapter4;

import java.util.ArrayList;
import java.util.Scanner;

public class A7PrimeFactorization {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Prints the prime factors for a given integer
	 */
	static void printPrimeFactors() {
		System.out.print("Enter a number to calculate prime factors from: ");
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		s.close();
		ArrayList<Integer> result = primeFactorization(n);
		System.out.println(result);
	}

	/**
      * Calculates the prime factors that make up the number n.
      * If you multiply them, you get the number.
      * The numbers are returned in an array list that has so many elements
      * as n has prime factors. They are sorted in ascending order.
      *
      * @param n The number to be partitioned
      * @return The prime factors in an ArrayList
      * 
	 */
	static ArrayList<Integer> primeFactorization(int n) {
		ArrayList<Integer> primeFactors = new ArrayList<Integer>();
		for (int i = 2; i <= n; i++) {
			while (n % i == 0) {
				if (i != 0 || i != 1)
					primeFactors.add(i);
				n = n / i;
			}
		}
		return primeFactors;
	}

}
