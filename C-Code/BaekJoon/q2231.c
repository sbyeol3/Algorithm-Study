#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int i, N, tmp, cnt=1, sum=0, constructor=0;
	scanf("%d", &N);
	tmp = N;

	while (tmp) {
		tmp /= 10;
		cnt++;
	}

	for (i = N - 9 * cnt; i < N; i++) {
		sum = tmp = i;
		while (tmp) {
			sum += tmp % 10;
			tmp /= 10;
		}
		if (sum == N) {
			constructor = i;
			break;
		}
	}

	printf("%d\n", constructor);
}