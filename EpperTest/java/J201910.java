package prev;

import java.util.Scanner;
import java.util.ArrayList;
public class J201910 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = sc.nextInt();
		ArrayList<String> destinations = new ArrayList<String>();
		ArrayList<Character> possible = new ArrayList<Character>();
		
		for (int i=0;i<count+1;i++) {
			String dest = sc.nextLine();
			destinations.add(dest);
		}
		
		String initial = sc.nextLine();
		int pos = initial.length();
		
		for (String dest : destinations) {
			if (dest.startsWith(initial) && dest.length() > pos) {
				char ch = dest.charAt(pos);
				possible.add(ch);
			}
		}
		
		String keyboard = "***";
		for (int i='A'; i<='Z'; i++) {
			char ch = (char)i;
			if (possible.contains(ch)) keyboard += ch;
			else keyboard += '*';
			if (i % 8 == 5) keyboard += '\n';
		}
		keyboard += "***";
		System.out.println(keyboard);
		sc.close();
	}

}
