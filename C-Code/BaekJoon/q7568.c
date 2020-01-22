#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, j, N;
	int* weight, * height, *grade;

	scanf("%d", &N);
	weight = (int*)malloc(sizeof(int) * N);
	height = (int*)malloc(sizeof(int) * N);
	grade = (int*)malloc(sizeof(int) * N);

	for (i = 0; i < N; i++) {
		scanf("%d %d", &weight[i], &height[i]);
		grade[i] = 1;
	}

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			if (weight[i] < weight[j] && height[i] < height[j]) grade[i]++;

	for (i = 0; i < N; i++)
		i==N-1? printf("%d", grade[i]):printf("%d ", grade[i]);

	free(weight); free(height); free(grade);
	putchar('\n');
}