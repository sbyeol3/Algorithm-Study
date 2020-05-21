#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int i, j, T, N, M;
	int bridge[31][31] = { 0, };
	scanf("%d", &T);

	for (i = 0; i < 31; i++) {
		bridge[i][i] = bridge[i][0] = 1;
		for (j = 1; j <= i - 1; j++)
			bridge[i][j] = bridge[i - 1][j - 1] + bridge[i - 1][j];
	}

	for (i = 0; i < T; i++){
		scanf("%d %d", &N, &M);
		printf("%d\n", bridge[M][N]);
	}
}