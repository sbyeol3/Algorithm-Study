#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
// ���� ��ҹ��ڿ� ���⸸���� �̷���� ������ �־�����. �� ���忡�� �� ���� �ܾ ������? �̸� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
// ��, �ܾ�� ���� �ϳ��� ���еȴٰ� �����Ѵ�.

int main() {
	char str[100];
	int cnt = 0;
	printf("���� �Է� : "); gets(str);

	for (int i = 0; str[i] != '\0'; i++)
		str[i] == ' ' ? cnt++ : 1;
	printf("�ܾ��� ���� : %d\n",++cnt);
}