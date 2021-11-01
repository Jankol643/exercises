package Chapter7_Lists_Sets_Maps;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Ex07_SetOperations {
    public static void main(String[] args) {
        Collection<Integer> collection1 = Arrays.asList(1, 2, 4, 7, 8);
        Collection<Integer> collection2 = Arrays.asList(2, 3, 7, 9, 7);
        Set<Integer> result = findCommon(collection1, collection2);
        System.out.println(result);
        Set<Integer> result2 = findCommonWithoutJDK(collection1, collection2);
        System.out.println(result2);
    }

    static <T> Set<T> findCommon(final Collection<T> collection1, final Collection<T> collection2) {
        Set<T> result = new HashSet<>();
        result.addAll(collection1);
        result.retainAll(collection2);
        return result;
    }

    static <T> Set<T> findCommonWithoutJDK(final Collection<T> collection1, final Collection<T> collection2) {
        Set<T> result = new HashSet<>();
        for (T elem1 : collection1) {
            for (T elem2 : collection2) {
                if (elem1 == elem2)
                    result.add(elem1);
            }
        }
        return result;
    }

    static <T> Set<T> difference(final Collection<T> collection1, final Collection<T> collection2) {
        Set<T> result = new HashSet<>(collection1);
        result.removeAll(collection2);
        return result;
    }

    static <T> Set<T> union(final Collection<T> collection1, final Collection<T> collection2) {
        Set<T> result = new HashSet<>(collection1);
        result.addAll(collection2);
        return result;
    }

    static <T> Set<T> intersection(final Collection<T> collection1, final Collection<T> collection2) {
        Set<T> result = new HashSet<>(collection1);
        result.retainAll(collection2);
        return result;
    }

}
