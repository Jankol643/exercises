package chapter4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class A6_NumberStatistics {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	

	/**
	 * Prints the minimum, maximum and average from a line of numbers read from a
	 * file
	 */
	public static void numberStatistics() {
		// read first line of file
		String filename = "4_numberStatistics.txt";
		filename = "resources/" + filename;
		String data = "";
		try {
			File myObj = new File(filename);
			Scanner myReader = new Scanner(myObj);
			data = myReader.nextLine();
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("File could not be found.");
			e.printStackTrace();
		}

		// assuming that data is a space separated string of integers
		String[] strArray = data.split(" ");
		System.out.println(data);
		int[] intArray = new int[strArray.length];
		int i = 0;
		for (String token : strArray) {
			intArray[i++] = Integer.parseInt(token);
		}

		int max = 0;
		int min = 0;
		int sum = 0;
		int count = intArray.length;

		for (int number : intArray) {
			if (number < min)
				min = number;
			else if (number > max) {
				max = number;
			}
			sum += number;
		}

		float avg = sum / count;
		System.out.println("minimum: " + min);
		System.out.println("maximum: " + max);
		System.out.println("average: " + avg);
	}

}
