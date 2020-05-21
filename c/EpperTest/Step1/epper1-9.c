#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 두 정수를 입력받고 조건연산자( ? : )를 이용하여  더 큰 수를 출력하는 프로그램을 작성하여라.
int main() {
	int x, y;
	printf("두 정수를 입력하시오\n");
	scanf("%d\n%d", &x, &y);
	printf("두 수 <%d, %d> 중에서 큰 수 : %d \n", x, y, (x > y ? x : y));
}