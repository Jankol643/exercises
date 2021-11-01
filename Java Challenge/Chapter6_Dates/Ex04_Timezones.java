package Chapter6_Dates;

import java.sql.Timestamp;
import java.time.ZoneId;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class Ex04_Timezones {
    public static void main(String[] args) {
        Timestamp start1 = new Timestamp(System.currentTimeMillis());
        Set<String> result = selectedAmericanAndEuropeanTimeZones();
        Timestamp end1 = new Timestamp(System.currentTimeMillis());
        System.out.println(end1.getTime() - start1.getTime());
        Timestamp start2 = new Timestamp(System.currentTimeMillis());
        Set<String> result2 = selectedAmericanAndEuropeanTimeZones2();
        Timestamp end2 = new Timestamp(System.currentTimeMillis());
        System.out.println(end2.getTime() - start2.getTime());
    }

    static Set<String> selectedAmericanAndEuropeanTimeZones() {
        Set<String> result = new TreeSet<String>();
        Set<String> allZones = ZoneId.getAvailableZoneIds();
        for (String zone : allZones) {
            if (zone.startsWith("America/L") || zone.startsWith("Europe/S"))
                result.add(zone);
        }
        return result;
    }

    static Set<String> selectedAmericanAndEuropeanTimeZones2()
    {
        final Set<String> allZones = ZoneId.getAvailableZoneIds();
        final Predicate<String> inEuropeS = name -> name.startsWith("Europe/S");
        final Predicate<String> inAmericaL = name -> name.startsWith("America/L");
        final Predicate<String> europeOrAmerica = inEuropeS.or(inAmericaL);

        return allZones.stream().filter(europeOrAmerica).collect(Collectors.toCollection(TreeSet::new));
    }
}
