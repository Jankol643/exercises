package Chapter4_strings;

import java.util.Arrays;
import java.util.List;

public class Ex02_Joiner {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("Micha", "Zürich");
        String separator = " likes ";
        String result = join(list, separator);
        System.out.println(result);
        String result2 = joinStrings(list, separator);
        System.out.println(result2);
    }

    static String join(List<String> list, String separator) {
        String result = "";
        for (int i = 0; i < list.size(); i++) {
            result += list.get(i);
            if (i != list.size() - 1)
                result += separator;
        }
        return result;
    }

    static String joinStrings(List<String> list, String separator) {
        String result = "";
        for (int i = 0; i < list.size(); i++) {
            result = result.concat(list.get(i));
            if (i != list.size() - 1)
                result = result.concat(separator);
        }
        return result;
    }
}