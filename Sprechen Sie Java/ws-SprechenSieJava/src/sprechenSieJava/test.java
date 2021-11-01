package sprechenSieJava;

public class test {

    public static void main(String[] args) {
        int iterations = 100;
        long[] fact = new long[iterations];
        fact[0] = 1; fact[1] = 1;
        for (int i = 2; i <= iterations; i++) {
            long k = 1;
            for (int j = 1; j <= i; j++) {
                k = k * j;
            }
            fact[i] = k;

            System.out.println(fact[i]);
        }
    }

}
