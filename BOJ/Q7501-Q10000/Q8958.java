import java.util.Scanner;

public class OX8958 {
	static final int MAX = 10000;
	static int scr[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		int score=0, cnt=0;
		
		for(int j=0;j<num;j++) {
			String str = s.next();
			for(int i=0;i<str.length();i++) {
				if(str.charAt(i)=='O') {
					cnt++;
					score+=cnt;
				}
				else
					cnt=0;
			}
			scr[j] = score;
			score = 0;
			cnt = 0;
		}

		s.close();
		for(int j=0;j<num;j++)
			System.out.println(scr[j]);
	}

}
