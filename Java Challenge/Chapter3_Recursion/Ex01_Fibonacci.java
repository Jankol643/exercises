package Chapter3_Recursion;

public class Ex01_Fibonacci {
    public static void main(String[] args) {
        long result = fibRec(8);
        System.out.println(result);
    }

    static long fibRec(int maxValue) {
        if (maxValue > 10000)
            throw new IllegalArgumentException("Values over 10000 are not allowed because of recursion (StackOverflowError)");
            
        if (maxValue == 1 || maxValue == 2)
            return 1;
        
        return fibRec(maxValue - 1) + fibRec(maxValue - 2);
    }
}
