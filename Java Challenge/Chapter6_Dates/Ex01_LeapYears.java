package Chapter6_Dates;

public class Ex01_LeapYears {
    public static void main(String[] args) {
        boolean leap = isLeap(1901);
        System.out.println(leap);
    }

    static boolean isLeap(int year) {
        if (year % 4 == 0)
            if (year % 100 != 0)
                return true;
            if (year % 400 == 0)
                return true;
            return false;
    }
}
