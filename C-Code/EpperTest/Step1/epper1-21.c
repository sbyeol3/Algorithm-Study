#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
// ������ ������ ���ڿ��� �Է¹޾� �и��Ͽ� ����ϴ� ���α׷��� �ۼ��ϼ���. (��, ���ڿ��� ���̴� 100�� �����̴�.)

int main() {
	char str[101];
	printf("������ �Է��ϼ��� : ");
	gets(str);

	for (int i = 0; i < strlen(str); i++)
		str[i] == ' ' ? printf("\n") : printf("%c",str[i]);
	putchar('\n');
}