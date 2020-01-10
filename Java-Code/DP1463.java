import java.util.Arrays;
import java.util.Scanner;

public class DP1463 { // top-down
	static final int MAX = 1000001;
	static int dp[] = new int[MAX];
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		int X = s.nextInt();
		s.close();
		
		Arrays.fill(dp, -1);
		System.out.println(make1(X));
		
	}
	
	static int make1 (int x) {
		if(x==1) return 0; 
		if(dp[x]!= -1) return dp[x]; 
		
		int result = make1(x-1)+1;
		
		if(x%3==0) result=Math.min(result, make1(x/3)+1);
		if(x%2==0) result=Math.min(result, make1(x/2)+1);
		dp[x]=result;
		return result;
	}
}
