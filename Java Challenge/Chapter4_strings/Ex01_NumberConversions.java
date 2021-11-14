package Chapter4_strings;

public class Ex01_NumberConversions {
    public static void main(String[] args) {
        int result = binaryToDecimal("111");
        System.out.println(result);
        int result2 = hexToDecimal("AB");
        System.out.println(result2);
    }

    static boolean isBinaryNumber(String str) {
        boolean binary = false;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            final char zero = '0';
            final char one = '1';
            if (c == zero || c == one)
                binary = true;
            else
                return false;
        }
        return binary;
    }

    static int binaryToDecimal(String str) {
        int decimal = 0;
        boolean isBinary = isBinaryNumber(str);
        if (isBinary) {
            int number = Integer.valueOf(str);
            int tmp = 0;
            int count = 0;
            while (number > 0) {
                tmp = number % 10;
                decimal = decimal + (int) (tmp * Math.pow(2, count));
                count++;
                number /= 10;
            }
            return decimal;
        } else
            throw new IllegalArgumentException("Entered number" + str + " is not a valid binary number");
    }

    static int hexToDecimal(String hexString) {
        String hstring = "0123456789ABCDEF";
        String hexStringUpper = hexString.toUpperCase();
        for (int i = 0; i < hexStringUpper.length(); i++) {
            if (hstring.indexOf(hexStringUpper.charAt(i)) == -1)
                throw new IllegalArgumentException("Entered number" + hexStringUpper + " is not a valid hexadecimal number");
        }
        int num = 0;
        for (int i = 0; i < hexStringUpper.length(); i++) {
            char ch = hexStringUpper.charAt(i);
            int n = hstring.indexOf(ch);
            num = 16 * num + n;
        }
        return num;
    }



}
