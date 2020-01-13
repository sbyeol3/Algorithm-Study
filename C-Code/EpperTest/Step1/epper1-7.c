#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 두 정수를 입력받아 더하기, 빼기, 곱하기, 나누기, 나머지연산을 수행하는 프로그램을 작성하시오.
int main() {
	int num1, num2;
	printf("정수1을 입력하세요 : "); scanf("%d", &num1);
	printf("정수2를 입력하세요 : "); scanf("%d", &num2);
	printf("%d + %d = %d\n", num1, num2, num1 + num2);
	printf("%d - %d = %d\n", num1, num2, num1 - num2);
	printf("%d * %d = %d\n", num1, num2, num1 * num2);
	printf("%d / %d = %d\n", num1, num2, num1/num2);
	printf("%d %% %d = %d\n", num1, num2, num1%num2); // '%' 기호 자체 1개 출력하려면 %%
}