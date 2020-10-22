package step1;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Scanner;
public class Q2569 {

	public static void main(String[] args) {
		HashMap<String, ArrayList<String>> database = new HashMap<String, ArrayList<String>>();
		Scanner sc = new Scanner(System.in);
		int input = 1;
		while(input != 0) {
			System.out.println("등록하려면 1번, 찾기하려면 2번, 삭제하려면 3번, 수정하려면 4번");
			input = sc.nextInt();
			switch(input) {
				case 1: {
					System.out.println("이름, 전화번호, 나이, 주소를 순서대로 입력하세요.");
					String name = sc.next();
					String tel = sc.next();
					String age = sc.next();
					String addr = sc.next();
					ArrayList<String> value = new ArrayList<String>() {{
						add(tel);
						add(age);
						add(addr);
					}};
					database.put(name, value);
					break;
				}
				case 2: {
					System.out.println("검색할 이름을 입력하세요.");
					String name = sc.next();
					ArrayList<String> value = database.get(name);
					System.out.println("다음과 같은 결과를 찾았습니다.");
					System.out.println(name);
					for (String s : value) {
						System.out.println(s);
					}
					break;
				}
				case 3: {
					System.out.println("삭제할 이름을 입력하세요.");
					String name = sc.next();
					database.remove(name);
					break;
				}
				case 4: {
					System.out.println("수정할 이름을 입력하세요.");
					String name = sc.next();
					System.out.println("전화번호, 나이, 주소를 순서대로 입력하세요.");
					String tel = sc.next();
					String age = sc.next();
					String addr = sc.next();
					ArrayList<String> newValue = new ArrayList<String>() {{
						add(tel);
						add(age);
						add(addr);
					}};
					database.replace(name, newValue);
					break;
				}
				default : {
					System.out.println("잘못된 값을 입력했습니다.");
					break;
				}
			}
		}
	}

}
