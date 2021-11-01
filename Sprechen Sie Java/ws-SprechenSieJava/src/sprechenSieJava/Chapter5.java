package sprechenSieJava;

public class Chapter5 {
    public static void main(String[] args) {
        calculatePi(5);
        double pi = pi();
        System.out.println(pi);
    }

    /**
     * Calculates Pi using an approximation
     * 
     * @param n precision to calculate
     */
    public static void calculatePi(int n) {
        double pi;
        double sum = 0;
        for (int i = 0; i <= n; i++) {
            sum = sum + (Math.pow(-1, i) / (2 * i + 1));
        }
        pi = 4 * sum;
        System.out.println(pi);
    }

    static double pi() {
        double n = 1.0, n0 = 0.0;
        int i = 3, sign = -1;
        while (Math.abs(n - n0) > 0.0000025) { // 0.00001 / 4
            n0 = n;
            n = n + sign * (1.0 / i);
            sign = -sign;
            i = i + 2;
        }
        return 4 * n;
    }

    public static double arcSinus(int iterations) {
        double arcSinus = 0;
        int[] fact = new int[iterations];
        for (int i = 0; i < iterations; i++) {
            for (int j = 1; j <= i; j++) {
                fact[i] = fact[i] * j;
            }
            System.out.println(fact(i));
        }
        /*
        fact[0] = 1; fact[1] = 1;
        for (int i = 0; i < iterations; i++) {
            arcSinus = arcSinus + ()
        }*/
        return arcSinus;
    }
}
