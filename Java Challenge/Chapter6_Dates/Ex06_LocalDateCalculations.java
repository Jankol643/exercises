package Chapter6_Dates;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class Ex06_LocalDateCalculations {
	public static void main(String[] args) {
		LocalDate firstJan2013 = LocalDate.of(2013, 1, 1);
		LocalDate lastDec2015 = LocalDate.of(2015, 12, 31);

		List<LocalDate> result = allFriday13th(firstJan2013, lastDec2015);
		System.out.println(result);
		Map<Integer, List<LocalDate>> result2 = friday13thGrouped(firstJan2013, lastDec2015);
		System.out.println(result2);
	}

	static List<LocalDate> allFriday13th(LocalDate startDate, LocalDate endDate) {
		List<LocalDate> result = new ArrayList<LocalDate>();
		long days = Math.abs(ChronoUnit.DAYS.between(startDate, endDate));
		for (int i = 0; i < (int) (days); i++) {
			LocalDate newDate = startDate.plusDays(i);
			// System.out.println(newDate);
			DayOfWeek friday = DayOfWeek.FRIDAY;
			if (newDate.getDayOfWeek().equals(friday) && newDate.getDayOfMonth() == 13)
				result.add(newDate);
		}
		return result;
	}

	static Map<Integer, List<LocalDate>> friday13thGrouped(final LocalDate start, final LocalDate end) {
		return new TreeMap<>(allFriday13th(start, end).stream().collect(Collectors.groupingBy(LocalDate::getYear)));
	}

}
