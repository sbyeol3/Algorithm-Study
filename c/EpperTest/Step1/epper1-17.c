#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	

// 임의의 두 정수 A, B를 입력받아 A의 약수의 합이 B의 배수가 되는지 구하시오.
int main() {
	int A, B, sumA=0;
	printf("정수 A ? "); scanf("%d", &A);
	printf("정수 B ? "); scanf("%d", &B);
	
	for (int i = 1; i <= A; i++)
		if (A % i == 0) sumA += i;

	printf("A의 약수의 합 : %d\n", sumA);
	sumA% B == 0 ? printf("%d은 %d(B)의 배수입니다.\n", sumA, B) : printf("%d은 %d(B)의 배수가 아닙니다.\n", sumA, B);
}