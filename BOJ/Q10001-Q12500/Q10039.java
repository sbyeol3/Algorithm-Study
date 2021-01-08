import java.util.Scanner;

public class Score10039 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num = 0;
		int scr = 0;
		
		for(int i=0;i<5;i++) {
			scr = s.nextInt();
			if(scr<40)
				num+=40;
			else
				num+=scr;
		}
		s.close();
		System.out.println(num/5);
	}

}
