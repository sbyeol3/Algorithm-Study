import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		
		int a1=(a%10)*100+(a%100-a%10)+a/100;
		int b1=(b%10)*100+(b%100-b%10)+b/100;
		
		System.out.println(Math.max(a1, b1));
	}

}