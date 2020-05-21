import java.util.Arrays;
import java.util.Scanner;

public class Stic9465 { // 더 풀어보기

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int T = s.nextInt();
		
		int value[][] = new int[2][100000];
		int result[] = new int[100000];
		int a[] = new int[10000000];
		int b[] = new int[10000000];
		int num = 0;
		
		for(int i=0;i<T;i++) {
			num = s.nextInt();
			for(int j=0;j<2;j++) {
				for(int k=0;k<num;k++) {
					value[j][k]=s.nextInt();
					if((j+k)%2==0)
						a[k] = value[j][k];
					else
						b[k] = value[j][k];
				}
			}
			if(num==1) {
				result[i] = Math.max(value[0][0], value[1][0]);
				break;
			}

			a[1] += a[0];
			b[1] += b[0];
			

			for(int x=2;x<num;x++) {
				a[x] += Math.max(a[x-1], b[x-2]);
				b[x] += Math.max(b[x-1], a[x-2]);
			}
			
			result[i] = Math.max(a[num-1], b[num-1]);
			Arrays.fill(a, 0);
			Arrays.fill(b, 0);
		}
		
		
		for(int i=0;i<T;i++)
			System.out.println(result[i]);
	}

}
