#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//�ϳ��� ���ڸ� �Է¹޾� ����ϴ� ���α׷��� �Լ� getchar()�� putchar()�� �̿��Ͽ� �ۼ��Ͻÿ�.
int main() {
	int ch;
	printf("���ڸ� �ϳ� �Է��ϼ��� : ");
	ch = getchar();
	printf("�Էµ� ���ڴ� : ");
	putchar(ch);
	putchar('\n');
}