package Chapter6_Dates;

public class Ex01_LeapYears {
    public static void main(String[] args) {
        boolean leap = isLeap(1901);
        System.out.println(leap);
    }

    static boolean isLeap(int year) {
        boolean leap1 = year % 4 == 0 && year % 100 != 0;
        boolean leap2 = year % 4 == 0 && year % 400 == 0;
        if (leap1 || leap2)
            return true;
        return false;
    }
}
