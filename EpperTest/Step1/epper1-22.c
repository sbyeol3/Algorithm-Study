#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//����ڷκ��� �� ������ �Է� �޾� �ŵ� ���� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�
// �� �� ����ڷκ��� ������ �Է� �޴� �Լ� int get_ingeter(void)��
// �ŵ����� ���� ���ϴ� �Լ� int power(int x, int y)�� ����� ����� ��.

int get_integer(void) {
	int num;
	printf("������ �Է��Ͻÿ� : ");
	scanf("%d", &num);
	return num;
}

int power(int x, int y) {
	int num = 1;
	while (y-- > 0)
		num *= x;
	return num;
}

int main() {
	int num1 = get_integer();
	int num2 = get_integer();
	int result = power(num1, num2);
	printf("%d�� %d���� %d�Դϴ�.\n", num1, num2, result);
}