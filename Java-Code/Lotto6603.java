import java.io.IOException;
import java.util.Scanner;

public class Lotto6603 {
	static int arr[];
	static int k;
	static int cnt;
	static StringBuffer sb;
	public static void main(String[] args) throws IOException {
		sb = new StringBuffer();
		Scanner s = new Scanner(System.in);
		
		do {
			k=s.nextInt();
			arr = new int[k];
			
			for(int i=0;i<k;i++)
				arr[i]=s.nextInt();
			
			for(int i=0;i<k;i++) {
				cnt=1;
				dfs(i,arr[i]+" ");
			}
			sb.append("\n");
		}while(k != 0);
			
		System.out.println(sb.toString());
		s.close();
	}
	
	public static void dfs(int v, String str) {
		if(cnt==6)
			sb.append(str+"\n");
		else {
			for(int i=v+1;i<k;i++) {
				++cnt;
				dfs(i,str+arr[i]+" ");
			}
		}
		cnt--;
	}

}

