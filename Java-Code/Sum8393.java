import java.util.Scanner;

public class Sum8393 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n=s.nextInt();
		String num=s.next();
		s.close();
		int cnt=0;
		
		for(int i=0;i<n;i++)
			cnt+= Character.getNumericValue(num.charAt(i));
		
		System.out.println(cnt);
	}
}
