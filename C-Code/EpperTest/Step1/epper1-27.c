#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int year, half;
	float radiation = 100;
	printf("�ʱ� ���ɷ� : 100\n");
	printf("�ݰ���(��)�� �Է��ϼ��� : ");
	scanf("%d", &year);
	half = year;

	while (radiation > 10) {
		radiation /= 2;
		printf("%d�� �Ŀ� ���� �� : %.3f\n", year, radiation);
		year += half;
	}
	printf("1/10 ���ϱ��� �ɸ� �ð� : %d��\n", year-half);
}