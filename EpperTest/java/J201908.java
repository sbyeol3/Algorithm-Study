package prev;

import java.util.Scanner;
public class J201908 {
	public static void printArray(int[] array, int length) {
		for (int i=0; i<length;i++) {
			System.out.printf("%d ", array[i]);
		}
		System.out.println();
	}
	public static int ripenTomato(int[] tomatoes, int M, int N) {
		int length = M*N;
		for (int i=0;i<length;i++) {
			int top = (i-M > 0) ? i-M : -1;
			int left = (i%M != 0) ? i-1 : -1;
			int right = ((i+1)%M != 0) ? i+1 : -1;
			int down = (i+M < length) ? i+M : -1;
			
			if (tomatoes[i] == 0) {
				if ((top == -1 || tomatoes[top] == -1) && (down == -1 || tomatoes[down] == -1)) {
					if ((left == -1 || tomatoes[left] == -1) && (right == -1 || tomatoes[right] == -1))
						return -1;
				}
			}
		}
		
		int day = 0;
		int[] today = tomatoes.clone();
		while (true) {
			boolean allRipen = true;
			int[] nextDay = today.clone();
			for (int i=0;i<length;i++) {
				if (today[i] == 1) {
					if (i-M > 0 && nextDay[i-M] != -1) nextDay[i-M] = 1;
					if (i%M != 0 && nextDay[i-1] != -1) nextDay[i-1] = 1;
					if ((i+1)%M !=0 && nextDay[i+1] != -1) nextDay[i+1] = 1;
					if (i+M < length && nextDay[i+M] != -1) nextDay[i+M] = 1;
				} else if (today[i] == 0) allRipen = false;
			}
			today = nextDay;
			if (allRipen) break;
			day++;
		}
		return day;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		int[] tomatoes = new int[N*M];
		
		for (int i=0;i<N;i++) {
			for (int j=0;j<M;j++) {
				int state = sc.nextInt();
				int pos = i*M + j;
				tomatoes[pos] = state;
			}
		}
		
		int res = ripenTomato(tomatoes, M, N);
		System.out.println(res);
	}

}
