package prev;
import java.util.Scanner;
import java.util.Arrays;

public class J201903 {
	public static char solution(String str1, String str2) {
		int lenStr1 = str1.length(), lenStr2 = str2.length();
		if (lenStr1 != lenStr2) return 'F';
		char[] s1 = str1.toCharArray();
		char[] s2 = str2.toCharArray();
		Arrays.sort(s1);
		Arrays.sort(s2);
		return (Arrays.equals(s1,s2)) ? 'T' : 'F';
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] inputs = sc.nextLine().split(" ");
		String str1 = inputs[0].toLowerCase(), str2 = inputs[1].toLowerCase();
		char result = solution(str1, str2);
		System.out.println(result);
		sc.close();
	}

}
