#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// main �Լ����� ����ڷκ��� �� ������ �Է� �ް�,
// �����͸� ���ڷ� ������ ���� �� ���� ���� �ٲٴ� �Լ��� �ۼ��϶�.

void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

int main() {
	int* a, * b;
	printf("�� ������ �Է��Ͻÿ�\n");
	scanf("%d", &a); scanf("%d", &b);
	
	printf("a=%d b=%d\n", a, b);
	swap(&a, &b);
	printf("a=%d b=%d\n", a, b);
	return 0;
}