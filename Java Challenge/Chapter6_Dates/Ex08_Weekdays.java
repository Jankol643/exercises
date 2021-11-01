package Chapter6_Dates;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.temporal.TemporalAdjuster;
import java.time.temporal.TemporalAdjusters;
import java.util.Map;

public class Ex08_Weekdays {

    public static void main(String[] args) {
        weekdays();
    }

    public static void weekdays() {
        LocalDate convertedDate = LocalDate.parse("2019-12-24");
        DayOfWeek weekday = convertedDate.getDayOfWeek();
        System.out.println("24. Dezember 2019: " + weekday);

        weekday = convertedDate.with(TemporalAdjusters.firstDayOfMonth()).getDayOfWeek();
        System.out.println("First day of December 2019: " + weekday);
        
        weekday = convertedDate.with(TemporalAdjusters.lastDayOfMonth()).getDayOfWeek();
        System.out.println("Last day of December 2019: " + weekday);    
    }

    public static Map<String, LocalDate> firstAndLastFridayAndSunday(YearMonth ym) {
        TemporalAdjuster firstFriday = TemporalAdjusters.firstInMonth(DayOfWeek.FRIDAY);
        TemporalAdjuster firstSunday = TemporalAdjusters.firstInMonth(DayOfWeek.SUNDAY);
        TemporalAdjuster LastFriday = TemporalAdjusters.lastInMonth(DayOfWeek.FRIDAY);
        TemporalAdjuster LastSunday = TemporalAdjusters.lastInMonth(DayOfWeek.SUNDAY);

        
    }

}
