package step1;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Q2495 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cnt = 0, before = 0;
		while (true) {
			int ch = br.read();
			if (ch == ' ') {
				if (before != 0 && before != ' ') cnt++;
			}
			else if (ch == '\n') {
				if (before != 0 && before != ' ') cnt++;
				break;
			}
			before = ch;
		}
		System.out.println(cnt);
	}

}
