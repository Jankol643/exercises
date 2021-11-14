package chapter7;

import java.util.Scanner;

public class A2_MatrixManipulation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static void matrixManipulation() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a positive whole number: ");
		int n = scanner.nextInt();
		scanner.close();
		int[][] arr = readArray(n);
		boolean symmetry = checkMatrixSymmetry(arr);
		if (symmetry)
			transformMatrix(arr);
	}

	public static int[][] readArray(int n) {
		int[][] tmp = new int[n][n];
		for (int i = 0; i <= n; i++) {
			tmp[i] = inputArray();
		}
		int[][] arr = new int[n][n];
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++) {
				arr[i][j] = tmp[i][j];
			}
		}
		return arr;
		// array into form int[][]
	}
	
	public static boolean checkMatrixSymmetry(int[][] matrix) {
		boolean symmetrical = false;

		return symmetrical;
	}

	public static int[][] transformMatrix(int[][] matrix) {
		int length = matrix[0].length;
		int[][] result = new int[length][length];
		return result;
	}

}
