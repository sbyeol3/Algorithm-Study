import java.util.Arrays;
import java.util.Scanner;

public class Be2775 {
	static final int MAX = 999;
	static int num[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		int person[] = new int[T];
		int k, n;
		
		Arrays.fill(num, -1);
		for(int i=0;i<MAX;i++)
			num[i] = i;
		
		for(int i=0;i<T;i++) {
			k = s.nextInt();
			n = s.nextInt();
			
			if(num[k*14+n-1]!=-1)
				person[i] = num[k*14+n-1];
			
			if(k==0) {
				person[i] = n;
				continue;
			}
			//13*k+n-1
			else {
				for(int j=0;j<n+1;j++) {
					num[j] = j+1;	
				}
				for(int j=14;j<(14*k+n+1);j++) {
					if(j%14==0)
						num[j]=1;
					else
						num[j] = num[j-1]+num[j-14];
				}
				person[i] = num[14*k+n-1];
			}
		}
		
		for(int i=0;i<T;i++)
			System.out.println(person[i]);
	}
}
