#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	

// ������ ������ �Է¹޾� ���μ������� ����� ����ϼ���.
int main() {
	int num, i = 2;
	int primeFactor[100] = { 0, };
	printf("���� ? "); scanf("%d", &num);
	printf("%d = ", num);

	while (num > 1) {
		if (num % i == 0) {
			primeFactor[i]++;
			num /= i;
		}
		else i++;
	}

	for (int j = 0; j <= i; j++) {
		if (primeFactor[j] != 0) {
			if (primeFactor[j] == 1)
				printf("(%d*1)", j);
			else {
				printf("(");
				for (int k = 0; k < primeFactor[j]; k++)
					k < primeFactor[j] - 1 ? printf("%d*", j) : printf("%d)", j);
			}
		}
	}
	putchar('\n');
	return 0;
}