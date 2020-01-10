import java.io.*;
import java.util.Arrays;

public class DP1463_2 { // bottom-up
	static final int MAX = 1000001;
	static int dp[] = new int[MAX];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
		int X = Integer.parseInt(bf.readLine());
	
		Arrays.fill(dp, 10000000);
		
		dp[1] = 0; // base case
		for(int i=1; i<X; i++){
		        dp[i+1] = Math.min(dp[i+1], dp[i]+1);
		        if(i*2 < MAX) dp[i*2] = Math.min(dp[i*2], dp[i]+1);
		        if(i*3 < MAX) dp[i*3] = Math.min(dp[i*3], dp[i]+1);
		}// dp[i]에 도달했을 때에는 이미 dp[i-1]+1, dp[i/2]+1, dp[i/3]+1 중 최솟값이 구해져 있는 상태
		System.out.println(dp[X]);

	}

}
