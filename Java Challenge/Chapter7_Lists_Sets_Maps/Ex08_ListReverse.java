package Chapter7_Lists_Sets_Maps;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.Random;

public class Ex08_ListReverse {
    public static void main(String[] args) {
        int powers = 6;
        int n = (int)(Math.pow(10, powers));
        Integer[] list = new Integer[n];
        
        for (int i = 0; i < n; i++) {
            Random randomNum = new Random();
            Integer rand = (Integer)(randomNum.nextInt((100 - 0) + 1) + 0);
            list[i] = rand;
        }
        LinkedList<Integer> list1 = new LinkedList<Integer>(Arrays.asList(list));

        long start1 = System.nanoTime();
        List<Integer> result = reverse(list1);
        long end1 = System.nanoTime();
        long duration = end1 - start1;
        System.out.println(duration / 1000000);
        long start2 = System.nanoTime();
        List<Integer> result2 = listReverseWithListIterator(list1);
        long end2 = System.nanoTime();
        long duration2 = end2 - start2;
        System.out.println(duration2 / 1000000);
    }

    /**
     * Reverses a given list of elements
     * can handle a List<Integers> with 10^8 elements, much slower than second method for LinkedList<Integer> with 10^5 elements
     * @param <T>
     * @param originalList
     * @return
     */
    static <T> List<T> reverse(List<T> originalList) {
        List<T> result = new ArrayList<T>();
        for (int i = originalList.size() - 1; i >= 0; i--) {
            T elem = originalList.get(i);
            result.add(elem);
        }
        return result;
    }

    static <T> List<T> listReverseWithListIterator(final List<T> values) {
        final List<T> result = new ArrayList<T>();

        final ListIterator<T> it = values.listIterator(values.size());
        while (it.hasPrevious()) {
            result.add(it.previous());
        }
        return result;
    }
}
