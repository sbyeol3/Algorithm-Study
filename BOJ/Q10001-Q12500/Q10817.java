import java.util.Scanner;

public class Tnum10817 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num[] = new int[3];
		int temp;
		
		for(int i=0;i<3;i++) {
			num[i]=s.nextInt();
		}
		s.close();
		for(int i=1;i<3;i++) {
			if(num[i]<num[i-1]) {
				temp = num[i-1];
				num[i-1] = num[i];
				num[i] = temp;
			}
		}
		
		if(num[0]>num[1]) {
			temp = num[0];
			num[1] = num[0];
			num[1] = temp;
		}
		
		System.out.println(num[1]);
	}

}
