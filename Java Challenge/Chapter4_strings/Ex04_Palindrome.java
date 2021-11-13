package Chapter4_strings;

public class Ex04_Palindrome {
    public static void main(String[] args) {
        boolean result = isPalindrome("ABCBX");
        System.out.println(result);
    }

    static boolean isPalindrome(String str) {
        String UppercaseString = str.toUpperCase();
        int length = str.length();
        boolean isPalindrome = true;  
        
        for(int beginIndex = 0; beginIndex < length; beginIndex++)
        {
            if(str.charAt(beginIndex) != str.charAt(length-1-beginIndex)) {
                isPalindrome = false;
                break;
            }
        }
        return isPalindrome;
    }
}
