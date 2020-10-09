package prev;

import java.util.Scanner;

public class J201807 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] nums = new int[9];
		int sum = 0;
		int idx1 = 0, idx2 = 0;
		boolean find = false;
		
		for (int i=0;i<9;i++) {
			int num = sc.nextInt();
			nums[i] = num;
			sum += num;
		}
		
		for (int i=0;i<9;i++) {
			int num1 = nums[i];
			for (int j=i+1;j<9;j++) {
				int two = num1 + nums[j];
				if (sum - two == 100) {
					idx1 = i;
					idx2 = j;
					find = true;
					break;
				}
			}
			if (find) break;
		}
		
		for (int i=0;i<9;i++) {
			if (i == idx1 || i == idx2) continue;
			System.out.printf("%d ", nums[i]);
		}
		System.out.println();
		sc.close();
	}
}
