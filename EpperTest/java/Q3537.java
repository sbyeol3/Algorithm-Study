package step1;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Q3537 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int word, max = 0, count = 0, maxIdx = 0;
		int[] engChar = new int[26];
		
		while (true) {
			word = br.read();
			if (word == '\n') break;
			if (word <= 'Z') engChar[word-'A']++;
			else engChar[word-'a']++;
		}
		
		for(int i=0;i<26;i++) {
			int cnt = engChar[i];
			if (cnt > max) {
				count = 0;
				max = cnt;
				maxIdx = i;
			} else if (cnt == max) count++;
		}
		if (count != 0) System.out.println('?');
		else System.out.printf("%c\n", 'A'+ maxIdx);
	}

}
