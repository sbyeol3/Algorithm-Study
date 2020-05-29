import java.util.Scanner;

public class Arr1152 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str = s.nextLine();
		int cnt = 0;
		
		for(int i=0;i<str.length();i++) {
			if(str.charAt(i)==' ') {
				if(i!=0 && str.charAt(i-1)!=' ') cnt++;
			}
			if(i==str.length()-1 && str.charAt(i)!=' ')
				cnt++;
		}
		System.out.println(cnt);
		s.close();
	}
}