#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// �� ������ �Է¹޾� ���ϱ�, ����, ���ϱ�, ������, ������������ �����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main() {
	int num1, num2;
	printf("����1�� �Է��ϼ��� : "); scanf("%d", &num1);
	printf("����2�� �Է��ϼ��� : "); scanf("%d", &num2);
	printf("%d + %d = %d\n", num1, num2, num1 + num2);
	printf("%d - %d = %d\n", num1, num2, num1 - num2);
	printf("%d * %d = %d\n", num1, num2, num1 * num2);
	printf("%d / %d = %d\n", num1, num2, num1/num2);
	printf("%d %% %d = %d\n", num1, num2, num1%num2); // '%' ��ȣ ��ü 1�� ����Ϸ��� %%
}