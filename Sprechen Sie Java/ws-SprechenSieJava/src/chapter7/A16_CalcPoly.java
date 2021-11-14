package chapter7;

public class A16_CalcPoly {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * Calculates the value of a polynom with an arbitrary length of parameters
	 * @param params
	 * @return
	 */
	public static double poly(int x, int... params) {
		double y = 0;
		int count = params.length;
		for(int i = 0; i < params.length; i++) {
			int par = params[i];
			y = y + par * Math.pow(x, count - i);
		}
		return y;
	}

}
