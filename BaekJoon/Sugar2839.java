import java.util.Scanner;

public class Sugar2839 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int m, n; // N = 5*m + 3*n
		int sum=0;
		boolean able=false;
		
		if((N%5)%3==0) {
			m=N/5;
			n=(N%5)/3;
			sum=m+n;
		}
		else {
			for(int i=N/5;i>=0;i--) {
				if((N-5*i)%3==0) {
					m=i;
					n=(N-5*i)/3;
					sum=m+n;
					able=true;
					break;
				}			
			}
			if(able==false)
				sum=-1;
		}
			
		
		System.out.println(sum);
	}
}
