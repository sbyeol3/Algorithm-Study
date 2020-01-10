import java.util.Scanner;

public class Cy1110 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N=s.nextInt();
		s.close();
		int temp=N;
		int rNum=N;
		int cnt=0;
		
		do {
			rNum=temp%10;
			temp=temp/10+rNum;
			temp=rNum*10+temp%10;
			cnt++;
		}while(temp!=N);
		
		System.out.println(cnt);

	}

}
