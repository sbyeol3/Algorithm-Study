#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	

// ������ �� ���� A, B�� �Է¹޾� A�� ����� ���� B�� ����� �Ǵ��� ���Ͻÿ�.
int main() {
	int A, B, sumA=0;
	printf("���� A ? "); scanf("%d", &A);
	printf("���� B ? "); scanf("%d", &B);
	
	for (int i = 1; i <= A; i++)
		if (A % i == 0) sumA += i;

	printf("A�� ����� �� : %d\n", sumA);
	sumA% B == 0 ? printf("%d�� %d(B)�� ����Դϴ�.\n", sumA, B) : printf("%d�� %d(B)�� ����� �ƴմϴ�.\n", sumA, B);
}