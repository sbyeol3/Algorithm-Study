import java.util.Arrays;
import java.util.Scanner;

public class Num2577 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num[] = new int[10];
		int temp, cnt = 0;
		int A = s.nextInt();
		int B = s.nextInt();
		int C = s.nextInt();
		s.close();
		
		Arrays.fill(num, 0);
		int prod = A * B * C;
		
		temp = prod;
		while(temp>10) {
			temp/=10;
			cnt++;
		}
		
		for(int i=cnt;i>0;i--) {
			temp = (int)Math.pow(10,cnt--);
			num[prod/temp]++;
			prod %= temp;
		}
		
		num[prod]++;
		
		for(int i=0;i<10;i++)
			System.out.println(num[i]);
	}

}
