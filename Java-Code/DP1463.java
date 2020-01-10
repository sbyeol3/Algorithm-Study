import java.io.*;
import java.util.Arrays;

public class DP1463 { // top-down
	static final int MAX = 1000001;
	static int dp[] = new int[MAX];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
		int X = Integer.parseInt(bf.readLine());
	
		Arrays.fill(dp, -1);
		System.out.println(make1(X));
		
	}
	
	static int make1 (int x) {
		if(x==1) return 0; // base case
		if(dp[x]!= -1) return dp[x]; // 이미 계산한 case
		
		int result = make1(x-1)+1;
		
		if(x%3==0) result=Math.min(result, make1(x/3)+1);
		if(x%2==0) result=Math.min(result, make1(x/2)+1);
		dp[x]=result;
		return result;
	}
}
