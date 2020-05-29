#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h> // 동적할당

//두 행렬을 입력받아 덧셈과 뺄셈 연산의 결과를 출력하세요.
// 행렬의 덧셈과 뺄셈 연산이 불가능한 경우, "계산불능"을 출력하세요.

int main() {
	int colA, lowA, colB, lowB;
	int** matA, ** matB;

	printf("행렬 A의 행, 열의 수를 입력하세요 : ");
	scanf("%d %d", &colA, &lowA);

	matA = (int**)malloc(sizeof(int*) * colA);
	for (int i = 0; i < lowA; i++)
		matA[i] = (int*)malloc(sizeof(int) * lowA);

	printf("행렬 A의 값을 입력하세요.\n");
	for (int i = 0; i < colA; i++)
		for (int j = 0; j < lowA; j++)
			scanf("%d", &matA[i][j]);

	printf("행렬 B의 행, 열의 수를 입력하세요 : ");
	scanf("%d %d", &colB, &lowB);

	matB = (int**)malloc(sizeof(int*) * colB);
	for (int i = 0; i < lowB; i++)
		matB[i] = (int*)malloc(sizeof(int) * lowB);

	printf("행렬 B의 값을 입력하세요.\n");
	for (int i = 0; i < colB; i++)
		for (int j = 0; j < lowB; j++)
			scanf("%d", &matB[i][j]);

	if (lowA != lowB || colA != colB) printf("\n계산불능\n");
	else {
		printf("\nA + B 두 행렬의 덧셈\n");
		for (int i = 0; i < colA; i++) {
			for (int j = 0; j < lowA; j++)
				printf("%d ", matA[i][j] + matB[i][j]);
			printf("\n");
		}

		printf("\nA - B 두 행렬의 뺄셈\n");
		for (int i = 0; i < colA; i++) {
			for (int j = 0; j < lowA; j++)
				printf("%d ", matA[i][j] - matB[i][j]);
			putchar('\n');
		}
	}
}