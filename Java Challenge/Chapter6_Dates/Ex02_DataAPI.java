package Chapter6_Dates;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Period;

public class Ex02_DataAPI {
    public static void main(String[] args) {
        generateDateTime();
        timeDurations();
    }

    static void generateDateTime() {
        LocalDate birthday = LocalDate.parse("1999-10-19");
        LocalTime closingTime = LocalTime.parse("17:30");
        LocalDateTime now = LocalDateTime.now();
        Period OneYear10Months20Days = Period.of(1, 10, 20);
        Duration sevenHours15Minutes = Duration.ofHours(7).plusMinutes(15);
    }

    static void timeDurations() {
        LocalDate now = LocalDate.now();
        LocalDate birthday = LocalDate.of(1999, 10, 19);
        Period birthdayUntilNow = Period.between(birthday, now);
        Period nowUntilBirthday = Period.between(now, birthday);
        Period birthdayUntilNow2 = birthday.until(now);
        Period nowUntilBirthday2 = now.until(birthday);

        String birthdayUntilNowFormatted = formatPeriod(birthdayUntilNow);
        String nowUntilBirthdayFormatted = formatPeriod(nowUntilBirthday);
        String birthdayUntilNowFormatted2 = formatPeriod(birthdayUntilNow2);
        String nowUntilBirthdayFormatted2 = formatPeriod(nowUntilBirthday2);

        System.out.println("Birthday until now: " + birthdayUntilNowFormatted);
        System.out.println("Now until birthday: " + nowUntilBirthdayFormatted);

        System.out.println("Birthday until now: " + birthdayUntilNowFormatted2);
        System.out.println("Now until birthday: " + nowUntilBirthdayFormatted2);
    }

    static String formatPeriod(Period periodUnformatted) {
        String periodFormatted = "";
        if (periodUnformatted.getYears() != 0)
            periodFormatted += periodUnformatted.getYears() + " years" + ", ";
        if (periodUnformatted.getMonths() != 0)
            periodFormatted += periodUnformatted.getMonths() + " months" + ", ";
        if (periodUnformatted.getDays() != 0)
        periodFormatted += periodUnformatted.getDays() + " days";
        return periodFormatted;
    }
}
