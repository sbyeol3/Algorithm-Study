#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
// 공백을 포함한 문자열을 입력받아 분리하여 출력하는 프로그램을 작성하세요. (단, 문자열의 길이는 100자 이하이다.)

int main() {
	char str[101];
	printf("문장을 입력하세요 : ");
	gets(str);

	for (int i = 0; i < strlen(str); i++)
		str[i] == ' ' ? printf("\n") : printf("%c",str[i]);
	putchar('\n');
}