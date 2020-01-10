import java.util.Scanner;

public class Day1924 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String day[] = new String[]{"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
		int x = s.nextInt();
		int y = s.nextInt();
		int num = 0;
		s.close();
		
		if(x<2)
			num = y;

		else {
			num = 31;
			for(int i=2;i<x;i++) {
				if(i==2)
					num+=28;
				else if((i<8&&i%2==1) || (i>7&&i%2==0))
					num+=31;
				else
					num+=30;
			}
			num+=y;
		}
		System.out.println(day[num%7]);
	}
}
