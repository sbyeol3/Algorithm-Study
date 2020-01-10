import java.util.Scanner;

public class ACM10250 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		int ctm[] = new int[T];
		int H, W, N;
		int x,y;
		
		for(int i=0;i<T;i++) {
			H = s.nextInt();
			W = s.nextInt();
			N = s.nextInt();
			
			x = N%H; // 층 수 결정
			y = N/H; // 호 수 결정
			if(x==0) 
				ctm[i] = H*100+(y);
			else
				ctm[i] = x*100+(y+1);
		}
		s.close();
		for(int i=0;i<T;i++)
			System.out.println(ctm[i]);
	}

}
