#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num;
	float sum = 0;
	printf("정수를 입력하세요 : ");
	scanf("%d", &num);

	for (int i = 1; i <= num; i++) {
		printf("%d/%d ", i, i + 1);
		sum += (float)i /(float) (i + 1);
		i == num ? printf("= %.2f\n",sum) : printf("+ ");
	}
}