package Chapter6_Dates;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.Duration;
import java.time.ZonedDateTime;

public class Ex05_TimezoneCalc {
    public static void main(String[] args) {
        calculateTime();
    }

    static void calculateTime() {
        LocalDateTime zurich = LocalDateTime.of(2019, 9, 15, 13, 10);
        ZonedDateTime departureTime = zurich.atZone(ZoneId.of("Europe/Zurich"));
        Duration flightDuration = Duration.ofHours(11).plusMinutes(50);
        ZonedDateTime added = departureTime.plus(flightDuration);
        //ZonedDateTime addedZdt = added.atZone(ZoneId.of("America/Los_Angeles"));
        ZonedDateTime arrivalTime = added.withZoneSameInstant(ZoneId.of("America/Los_Angeles"));
        System.out.println(added);
        System.out.println(arrivalTime);
    }
}
