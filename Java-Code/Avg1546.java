import java.util.Scanner;

public class Avg1546 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N=s.nextInt();
		float score[] = new float[N];
		float max=0, cnt=0;
		
		for(int i=0;i<N;i++) {
			score[i] = s.nextInt();
			if(i==0)
				max = score[i];
			else {
				if(max<score[i])
					max = score[i];	
			}
		}
		s.close();
		for(int i=0;i<N;i++) {
			score[i]=(score[i]/max)*100;
			cnt+=score[i];
		}

		System.out.printf("%.2f\n",(float)cnt/N);
	}
}
