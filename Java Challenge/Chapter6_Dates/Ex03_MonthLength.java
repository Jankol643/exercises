package Chapter6_Dates;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

public class Ex03_MonthLength {
    public static void main(String[] args) {
        //calculations();
        monthLength();
    }

    static void calculations() {
        LocalDate date1 = LocalDate.of(2012, 2, 2);
        LocalDate date2 = LocalDate.of(2014, 2, 2);
        LocalDate date3 = LocalDate.of(2014, 4, 4);
        LocalDate date4 = LocalDate.of(2014, 5, 5);
        List<LocalDate> dates = Arrays.asList(date1, date2, date3, date4);

        for (int i = 0; i < 4; i++) {
            LocalDate date = dates.get(i);
            date = date.plusMonths(1);
            System.out.println(date);
        }
    }

    static void monthLength() {
        LocalDate date1 = LocalDate.of(2012, 2, 2);
        LocalDate date2 = LocalDate.of(2014, 2, 2);
        LocalDate date3 = LocalDate.of(2014, 4, 4);
        LocalDate date4 = LocalDate.of(2014, 5, 5);
        List<LocalDate> dates = Arrays.asList(date1, date2, date3, date4);

        for (int i = 0; i < 4; i++) {
            LocalDate date = dates.get(i);
            date = date.plusDays(date.lengthOfMonth());
            //date = date.plusDays(date.getMonth().length(date.isLeapYear()));
            System.out.println(date);
        }
    }
}