#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, M, i, j, k, max = 0, tmp = 0;
	int* card;
	scanf("%d %d", &N, &M);

	card = (int*)malloc(sizeof(int) * N);
	for (i = 0; i < N; i++)
		scanf("%d", &card[i]);

	for (i = 0; i < N-2; i++)
		for (j = i + 1; j < N-1; j++)
			for (k = j + 1; k < N; k++) {
				tmp = card[i] + card[j] + card[k];
				if (tmp == M) {
					max = tmp;
					break;
				}
				if (tmp > max && tmp<M) max = tmp;
			}

	printf("%d\n", max);
}