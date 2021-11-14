package chapter9;

import java.util.Scanner;

public class A4_EncodeRunLengthEncoding {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Reads a string and encodes it using run length encoding
	 */
	public static void encodeStringRLE() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a string: ");
		String str = scanner.nextLine();
		scanner.close();	
		
		String result = "";
		int occurence = 1;
		int lastOccurence = 0;
		for (int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			if (i < str.length() - 1 && c == str.charAt(i+1) && (int)(result[i-1]) < 9 ) {
				occurence += 1;
			}
			else {
				if (occurence > 1)
					result = result + c + occurence;
				lastOccurence = occurence;
				occurence = 1;
				result += c;
			}
		}
		System.out.println("Encoded String: " + result);
	}

}
