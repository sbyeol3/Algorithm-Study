import java.util.Scanner;

public class Dial5622 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str = s.nextLine();
		char[] chArr = str.toCharArray();
		int[] arr = new int[26];
		int cnt=0;
		
		for(int i=0;i<26;i++) {
			if(i<15)
				arr[i]=i/3+3;
			else if(i<19)
				arr[i]=8;
			else if(i<22)
				arr[i]=9;
			else
				arr[i]=10;
		}
		
		for(int i=0;i<str.length();i++) {
			cnt+=arr[chArr[i]-65];
		}
		
		System.out.println(cnt);
	}
	
}
