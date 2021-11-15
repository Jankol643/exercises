package chapter5;

public class A1CalcPi {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
    /**
     * Calculates Pi using an approximation
     * 
     * @param n precision to calculate
     */
    public static double calculatePi(int n) {
        double pi;
        double sum = 0;
        for (int i = 0; i <= n; i++) {
            sum = sum + (Math.pow(-1, i) / (2 * i + 1));
        }
        pi = 4 * sum;
        return pi;
    }

}
