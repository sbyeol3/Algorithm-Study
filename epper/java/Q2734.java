package step1;
import java.util.ArrayList;
public class Q2734 {
	public static int getDigits(int num) {
		String digits = Integer.toString(num);
		int total = 0;
		
		for (int i=0;i<digits.length();i++) {
			char digitChar = digits.charAt(i);
			int digit = Integer.parseInt(String.valueOf(digitChar));
			total += digit;
		}
		return total;
	}
	public static void searchNumber(ArrayList<Integer> list, int num) {
		int start = num;
		ArrayList<Integer> nums = new ArrayList<Integer>();
		
		while(true) {
			int newNum = start + getDigits(start);
			if (list.indexOf(newNum) != -1 || newNum > 10000) break;
			else {
				nums.add(newNum);
				start = newNum;
			}
		}
		
		for (int n : nums) {
			if (list.indexOf(n) == -1) list.add(n);
		}
	}
	public static void main(String[] args) {
		ArrayList<Integer> nonSelfNum = new ArrayList<Integer>();
		
		for(int i=1;i<10000;i++) {
			searchNumber(nonSelfNum, i);
		}
		
		System.out.println(1);
		for(int i=2;i<10000;i++) {
			if (nonSelfNum.indexOf(i) == -1) System.out.println(i);
		}
	}

}
