#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//하나의 문자를 입력받아 출력하는 프로그램을 함수 getchar()와 putchar()를 이용하여 작성하시오.
int main() {
	int ch;
	printf("문자를 하나 입력하세요 : ");
	ch = getchar();
	printf("입력된 문자는 : ");
	putchar(ch);
	putchar('\n');
}