package prev;
import java.util.ArrayList;
import java.util.Scanner;
public class J201809 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int width = sc.nextInt();
		int height = sc.nextInt();
		int shortWidth = width - 2, shortHeight = height - 2;
		int min = (width < height) ? width : height;
		
		ArrayList<Integer> possible = new ArrayList<Integer>();
		possible.add(1);
		sc.close();
		
		for (int i=2; i<=min ; i++) {
			if (width % i == 0) {
				if(shortHeight % i == 0) possible.add(i);
				else if ((width -2) % i == 0 && (height + 1) % i == 0) possible.add(i);
			}
			else if (height % i == 0) {
				if(shortWidth % i == 0) possible.add(i);
				else if ((height -2) % i == 0 && (width + 1) % i == 0) possible.add(i);
			}
			else if ((width -1) % i == 0 && (height - 1) % i == 0 ) possible.add(i);
		}
		
		for (Integer i : possible) {
			System.out.printf("%d ", i);
		}
	}

}
