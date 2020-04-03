import java.util.Scanner;

public class Str11721 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str=s.next();
		
		for(int i=0;i<str.length();i++) {
			System.out.print(str.charAt(i));
			if(i%10==9)
				System.out.println();
		}
	}

}
