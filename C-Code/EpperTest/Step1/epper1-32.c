#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int N, int* a) {
	int tmp = 0;
	for (int i = N; i > 0; i--)
		for (int j = 0; j < i-1; j++)
			if (a[j] > a[j + 1]) {
				tmp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = tmp;
			}
}

int main() {
	int N, *arr;
	printf("������ ���� : "); scanf("%d", &N);
	arr = (int*)malloc(sizeof(int) * N);

	printf("���� %d�� �Է� : ", N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	
	printf("���� ���� �� : ");
	for (int i = 0; i < N; i++)
		i == N - 1 ? printf("%d\n",arr[i]) : printf("%d ", arr[i]);

	bubbleSort(N, arr);
	printf("���� ���� �� : ");
	for (int i = 0; i < N; i++)
		i == N - 1 ? printf("%d\n", arr[i]) : printf("%d ", arr[i]);
}