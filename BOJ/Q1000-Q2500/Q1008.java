import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		double A = s.nextDouble();
		double B = s.nextDouble();
		s.close();
		
		System.out.println(A/B);
	}
}