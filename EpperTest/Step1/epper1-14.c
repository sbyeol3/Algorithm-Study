#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h> // �����Ҵ�

//�� ����� �Է¹޾� ������ ���� ������ ����� ����ϼ���.
// ����� ������ ���� ������ �Ұ����� ���, "���Ҵ�"�� ����ϼ���.

int main() {
	int colA, lowA, colB, lowB;
	int** matA, ** matB;

	printf("��� A�� ��, ���� ���� �Է��ϼ��� : ");
	scanf("%d %d", &colA, &lowA);

	matA = (int**)malloc(sizeof(int*) * colA);
	for (int i = 0; i < lowA; i++)
		matA[i] = (int*)malloc(sizeof(int) * lowA);

	printf("��� A�� ���� �Է��ϼ���.\n");
	for (int i = 0; i < colA; i++)
		for (int j = 0; j < lowA; j++)
			scanf("%d", &matA[i][j]);

	printf("��� B�� ��, ���� ���� �Է��ϼ��� : ");
	scanf("%d %d", &colB, &lowB);

	matB = (int**)malloc(sizeof(int*) * colB);
	for (int i = 0; i < lowB; i++)
		matB[i] = (int*)malloc(sizeof(int) * lowB);

	printf("��� B�� ���� �Է��ϼ���.\n");
	for (int i = 0; i < colB; i++)
		for (int j = 0; j < lowB; j++)
			scanf("%d", &matB[i][j]);

	if (lowA != lowB || colA != colB) printf("\n���Ҵ�\n");
	else {
		printf("\nA + B �� ����� ����\n");
		for (int i = 0; i < colA; i++) {
			for (int j = 0; j < lowA; j++)
				printf("%d ", matA[i][j] + matB[i][j]);
			printf("\n");
		}

		printf("\nA - B �� ����� ����\n");
		for (int i = 0; i < colA; i++) {
			for (int j = 0; j < lowA; j++)
				printf("%d ", matA[i][j] - matB[i][j]);
			putchar('\n');
		}
	}
}