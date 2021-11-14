package Chapter6_Dates;

import java.time.ZoneId;
import java.util.Set;
import java.util.TreeSet;

public class Ex04_Timezones {
    public static void main(String[] args) {
        Set<String> result = selectedAmericanAndEuropeanTimeZones();
        System.out.println(result);
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
    
}
