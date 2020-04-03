import java.util.Arrays;
import java.util.Scanner;

public class Fib1003 {
	static final int MAX = 1000;
	static int dp[] = new int[MAX];
	static int count0[] = new int[MAX];
	static int count1[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		int N[] = new int[T];
		
		for(int i=0;i<T;i++)
			N[i] = s.nextInt();
		Arrays.fill(count0, 0);
		Arrays.fill(count1, 0);
		Arrays.fill(dp, -1);
		
		for(int i=0;i<T;i++)
			fibCount(N[i]);
		
		for(int i=0;i<T;i++)
			System.out.println(count0[N[i]]+" "+count1[N[i]]);

	}
	static void fibCount(int n) {
		if(n==0) {
			count0[n] = 1;
			count1[n] = 0;
			dp[0] = 1;
			return;
		}
		else if(n==1) {
			count0[n] = 0;
			count1[n] = 1;
			dp[1] = 1;
			return;
		}
		
		if(dp[n-1]== -1)
			fibCount(n-1);

		count0[n]+=count0[n-1];
		count1[n]+=count1[n-1];

		if(dp[n-2]== -1)
			fibCount(n-2);
			
		count0[n]+=count0[n-2];
		count1[n]+=count1[n-2];

		dp[n] = 1;
	}
}
