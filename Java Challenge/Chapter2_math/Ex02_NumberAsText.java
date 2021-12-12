package Chapter2_math;
import java.util.Map;

public class Ex02_NumberAsText {
    public static void main(String[] args) {
        int n = 24680;
        String result = numberAsText(n);
        System.out.println("Input: " + n + ", " + "Output: " + result);
    }

    static final Map<Integer, String> digitToTextMap = Map.of(0, "ZERO", 1, "ONE", 2, "TWO", 3, "THREE", 4, "FOUR", 5, "FIVE",
            6, "SIX", 7, "SEVEN", 8, "EIGHT", 9, "NINE");

    static String numberAsText(final int n) {
        if (n < 0)
            throw new IllegalArgumentException("No negative values allowed.");

        String valueAsText = "";
        int temp = n;
        while (temp > 0) {
            int remainder = temp % 10;
            String remainderAsText = digitAsText(remainder); // convert last digit to text
            valueAsText = remainderAsText + " " + valueAsText;

            temp = temp / 10;
        }

        return valueAsText.trim();
    }

    static String digitAsText(int remainder) {
        remainder = remainder % 10;
        return digitToTextMap.getOrDefault(remainder, "-?-");
    }
}