#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 문자열을 입력받은 후, 입력받은 문자열에서 
// 알파벳 소문자, 알파벳 대문자, 숫자, 기호의 개수를 세어서 출력하는 프로그램을 작성하세요.

int main() {
	char str[100];
	int upper=0, lower=0, num=0, mark=0;
	printf("문자열을 입력하세요 : ");
	scanf("%[^\n]s", str);

	for (int i = 0; i < strlen(str); i++) { // 아스키코드 이용
		if ('A' <= str[i] && str[i] <= 'Z') upper++;
		else if ('a' <= str[i] && str[i] <= 'z') lower++;
		else if ('0' <= str[i] && str[i] <= '9') num++;
		else if (33 <= str[i] && str[i] <= 126) mark++;
	}
	printf("대문자 : %d\n", upper);
	printf("소문자 : %d\n", lower);
	printf("숫자 : %d\n", num);
	printf("기호 : %d\n", mark);
}