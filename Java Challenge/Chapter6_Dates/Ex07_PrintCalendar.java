package Chapter6_Dates;

import java.time.LocalDate;
import java.time.Month;

public class Ex07_PrintCalendar {
    public static void main(String[] args) {
        Month april = Month.APRIL;
        printCalendar(april, 2020);
    }

    static void printCalendar(Month month, int year) {
        System.out.println("Mo Di Mi Do Fr Sa So");
        LocalDate current = LocalDate.of(year, month, 1);
        
    }
}
