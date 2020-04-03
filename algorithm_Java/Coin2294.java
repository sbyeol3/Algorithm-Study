import java.util.Scanner;

public class Coin2294 {
	static final int MAX = 1001;
	static int coin[] = new int[MAX];
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int k = s.nextInt();
		
		for(int i=0;i<n;i++)
			coin[i] = s.nextInt();
		
		
		s.close();
		
		
	}

}
