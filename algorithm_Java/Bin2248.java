import java.util.Arrays;
import java.util.Scanner;

public class Bin2248 {
	static final int MAX = 32;
	static int bin[][] = new int[MAX][MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int L = s.nextInt();
		int I = s.nextInt();
		
		s.close();
		
		bin[1][1] = 2;
		
		for(int i=2; i<N+1;i++) {
			for(int j=1;j<L+1;j++) {
				if(j==1)
					bin[i][j] = bin[i-1][j]+1;
				else if(j==i)
					bin[i][j] = bin[i][j-1]+1;
				else
					bin[i][j] = bin[i-1][j-1] + bin[i-1][j];
			}
		}
		
		System.out.println(bin[N][L]);
		
	}

}
