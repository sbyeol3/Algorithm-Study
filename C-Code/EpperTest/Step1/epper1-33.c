#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
// 영어 대소문자와 띄어쓰기만으로 이루어진 문장이 주어진다. 이 문장에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
// 단, 단어는 띄어쓰기 하나로 구분된다고 생각한다.

int main() {
	char str[100];
	int cnt = 0;
	printf("문장 입력 : "); gets(str);

	for (int i = 0; str[i] != '\0'; i++)
		str[i] == ' ' ? cnt++ : 1;
	printf("단어의 개수 : %d\n",++cnt);
}