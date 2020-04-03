import java.util.Scanner;

public class Cycle1110 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int cnt = 0;
		int temp = N;
		
		if(N<10)
			temp = N*10 + N;
		else
			temp = (N%10)*10 +((N-N%10)/10 + N%10)%10;
		cnt++;
		
		while(N!=temp) {
			if(temp < 10) {
				temp = temp*10 + N;
			}
			else {
				temp = (temp%10)*10 +((temp-temp%10)/10 + temp%10)%10;
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
