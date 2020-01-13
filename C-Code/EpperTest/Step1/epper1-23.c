#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// 정수 5개를 저장 할 수 있는 배열을 선언하고 사용자로부터 정수를 5개 입력 받은 후 포인터를 사용하여 그 합을 구하는 프로그램을 작성하라.

int main() {
	int num[5];
	int i = 1, sum = 0;
	while (i < 6) {
		printf("정수 %d : ", i);
		scanf("%d", &num[i - 1]);
		sum += num[i-1];
		i++;
	}
	printf("총합 : %d\n", sum);
}