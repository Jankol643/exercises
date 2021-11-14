package chapter8;

import java.nio.charset.Charset;

public class A1_PrintHex {

	public static void main(String[] args) {

	}
	
	/**
	 * Prints an integer in its hexadecimal notation
	 * @param n int to print
	 */
	public static void printHex(int n) {
		String hex = Integer.toHexString(n);
		byte[] x = new byte[n];
		String str = new String(x, Charset.forName("UTF-16"));
		System.out.println("Hex1: " + str);
		System.out.println("Hex: " + hex);
	}

}
