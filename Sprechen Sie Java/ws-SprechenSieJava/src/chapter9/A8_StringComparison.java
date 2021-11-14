package chapter9;

public class A8_StringComparison {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	static int diff(String s1, String s2) {
		int result = 0;
		if (s1.length() < s2.length())
			result = -1;
		if (s1.equals(s2))
			result = 0;
		if (s1.length() > s2.length())
			result = 1;
		return result;
			
	}

}
