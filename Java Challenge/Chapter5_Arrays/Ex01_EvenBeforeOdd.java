package Chapter5_Arrays;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Ex01_EvenBeforeOdd {

    public static void main(String[] args) {
        int n = 7;
        int pow = (int)(Math.pow(10, n));
        int[] test1 = new int[pow];
        for (int i = 0; i < test1.length; i++) {
            Random rand = new Random();
            test1[i] = 0 + rand.nextInt(50 + 1);
        }
        Timestamp start = new Timestamp(System.currentTimeMillis());
        orderEvenBeforeOdd(test1);
        Timestamp end = new Timestamp(System.currentTimeMillis());
        long diff = end.getTime() - start.getTime();
        System.out.println(diff);
        Timestamp start2 = new Timestamp(System.currentTimeMillis());
        orderEvenBeforeOddOptimizedV2(test1);
        Timestamp end2 = new Timestamp(System.currentTimeMillis());
        long diff2 = end2.getTime() - start2.getTime();
        System.out.println(diff2);
    }

    public static void orderEvenBeforeOdd(int[] arr) {
        List<Integer> even = new ArrayList<Integer>();
        List<Integer> odd = new ArrayList<Integer>();

        for(int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0)
                even.add(arr[i]);
            else
                odd.add(arr[i]);
        }

        List<Integer> newList = new ArrayList<Integer>();
        
        newList.addAll(even);
        newList.addAll(odd);
        for(int i = 0; i < newList.size(); i++) arr[i] = newList.get(i);
    }

    static void swap(final int[] number, final int pos1, final int pos2)
    {
        final int temp = number[pos1];

        number[pos1] = number[pos2];
        number[pos2] = temp;
    }

    static void orderEvenBeforeOddOptimizedV2(final int[] numbers) {
        int left = 0;
        int right = numbers.length - 1;
        while (left < right)
        {
            // laufe bis zur ersten ungeraden Zahl oder Array-Ende
            while (left < numbers.length && numbers[left] % 2 == 0)
                left++;
            // laufe bis zur ersten geraden Zahl oder Array-Anfang
            while (right >= 0 && numbers[right] % 2 != 0)
                right--;

            if (left < right)
            {
                swap(numbers, left, right);
                left++;
                right--;
            }
        }
    }
}
