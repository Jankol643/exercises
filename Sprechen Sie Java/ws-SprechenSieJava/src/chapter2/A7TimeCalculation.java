package chapter2;

/**
 * @author janko
 *
 */
public class A7TimeCalculation {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Prints time in hours, minutes and seconds (h:m:s)
	 * @param seconds time in seconds
	 */
	public static void printFormattedTime(int seconds) {
		int hours = seconds / 3600;
		int rem = seconds - 3600*hours;
		int minutes = rem / 60;
		int printSeconds = rem - 60*minutes;
		System.out.println(hours + ":" + minutes + ":" + printSeconds);
	}

}
