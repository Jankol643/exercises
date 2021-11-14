package Chapter2_math;
import java.util.ArrayList;
import java.util.Scanner;

public class Ex04_PrimeNumbers {

    public static void main(String[] args) {
        System.out.print("List primes up to this int value: ");
        Scanner s = new Scanner(System.in);
        int maxValue = s.nextInt();
        s.close();
        ArrayList<Integer> result = calcPrimesUpTo(maxValue);
        System.out.println(result);
    }

    static ArrayList<Integer> calcPrimesUpTo(int maxValue) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 2; i < maxValue; i++) {
            boolean isPrime = checkPrime(i);
            if (isPrime)
                list.add(i);
        }
        return list;
    }

    static boolean checkPrime(int number) {
        boolean isPrime = false;
        ArrayList<Integer> divisors = new ArrayList<Integer>();
        double sqrtN = Math.sqrt(number);
        for (int i = 2; i < (int)(sqrtN + 1); i++) {
            if (number % i == 0) {
            	divisors.add(i);
            }
        }
        if (divisors.size() > 0)
        	isPrime = false;
        else
        	isPrime = true;
        
        return isPrime;
    }
}
