import java.util.Scanner;

public class Small10871 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int X = s.nextInt();
		
		int result[] = new int[N];
		int cnt=0;
		int num;
		
		for(int i=0;i<N;i++) {
			num = s.nextInt();
			if(num<X) {
				result[cnt]=num;
				cnt++;
			}
		}
		
		s.close();
		for(int i=0;i<cnt;i++) {
			System.out.print(result[i]);
			if(i!=cnt-1)
				System.out.print(" ");
		}

	}

}
