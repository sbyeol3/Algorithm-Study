import java.util.Arrays;
import java.util.Scanner;

public class B1904 {
	static final int MAX = 1000001;
	static int dp[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		
		Arrays.fill(dp, -1);
		System.out.println(tile01(N));
	}
	
	static int tile01(int n) {
		if(n==1) return 1;
		else if(n==2) return 2;
		if(dp[n]!= -1) return dp[n]; 
		int result =(tile01(n-1)+tile01(n-2))%15746;
		dp[n] = result;
		return result;
	}
}

