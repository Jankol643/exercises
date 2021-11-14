package chapter5;

public class A2_CalcArcSin {
	
    public static void main(String[] args) {

    }
	
    public static double arcSinus(int iterations) {
        double arcSinus = 0;
        int[] fact = new int[iterations];
        for (int i = 0; i < iterations; i++) {
            for (int j = 1; j <= i; j++) {
                fact[i] = fact[i] * j;
            }
            System.out.println(fact[i]);
        }
        return arcSinus;
    }
}