import java.util.Arrays;
import java.util.Scanner;

public class B2193 {
	static final int MAX = 100;
	static long dp[] = new long[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		
		Arrays.fill(dp, -1);
		System.out.println(pinary(N));
		
	}
	static long pinary (int x) {
		if(x==1) return 1;
		else if(x==2) return 1;
		if(dp[x]!= -1) return dp[x]; 
		
		long result = pinary(x-2) + pinary(x-1);

		dp[x]=result;
		return result;
	}

}
