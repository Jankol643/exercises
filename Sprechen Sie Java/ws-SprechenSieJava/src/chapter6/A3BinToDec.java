package chapter6;

public class A3BinToDec {

	public static void main(String[] args) {

	}
	
	/**
	 * Converts a binary number to a decimal number
	 * @param int bin binary number
	 * @return decimal number
	 * @throws IllegalArgumentException if input is not valid
	 */
	public static int binToDec(int bin) {
		String binS = Integer.toString(bin);
		if (binS.length() > 8 || bin < 0)
			throw new IllegalArgumentException();
		
		int decimalnumber = 0;
		int power = 0;
		while(bin > 0)
		{
			int temp = bin % 10; // last digit of number
			decimalnumber += temp * Math.pow(2, power);
			bin = bin / 10;
			power++;
		}
		return decimalnumber;
	}

}
