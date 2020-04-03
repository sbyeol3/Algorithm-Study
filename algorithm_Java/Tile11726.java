import java.util.Scanner;

public class Tile11726 {
	static final int MAX = 1001;
	static int tile[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		s.close();
		
		tile[1] = 1;
		tile[2] = 2;
		for(int i=3;i<n+1;i++) {
			tile[i] = (tile[i-2]+tile[i-1])%10007;
		}
		System.out.println(tile[n]);
	}
}
