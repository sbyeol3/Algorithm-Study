import java.util.Scanner;

public class Seq1065 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int tmp,cnt = 0;
		s.close();
		
		for(int i=1;i<(N+1);i++) {
			if(i<100) {
				cnt++;
				continue;
			}
			else{
				tmp = i%100;
				if((i/100-tmp/10)==(tmp/10-tmp%10))
					cnt++;
			}
		}
		
		System.out.println(cnt);
	}

}
