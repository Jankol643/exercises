package Chapter4_strings;

public class Ex03_ReverseString {
    public static void main(String[] args) {
        String res = reverse("PETER");
        System.out.println(res);
    }

    static String reverse(String str) {
        String result = "";
        char[] charArray = new char[str.length()];
        for (int i = str.length(); i > 0; i--) {
            char c = str.charAt(i-1);
            charArray[str.length()-i] = c;
        }
        result = String.valueOf(charArray);
        return result;
    }
}
