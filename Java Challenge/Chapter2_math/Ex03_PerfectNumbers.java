package Chapter2_math;
import java.util.ArrayList;

public class Ex03_PerfectNumbers {

    public static void main(String[] args) {
        ArrayList<Integer> res = calcPerfectNumbers(1000);
        System.out.println(res);
    }

    static ArrayList<Integer> calcPerfectNumbers(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i = 2; i < n; i++) {
            if (isPerfectNumberSimple(i) == true)
                list.add(i);
        }
        return list;
    }

    static boolean isPerfectNumberSimple(final int number)
    {
        // immer durch 1 teilbar
        int sumOfMultipliers = 1;
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0)
                sumOfMultipliers += i;
        }

        if (sumOfMultipliers == number)
            return true;
        return false;
    }
}