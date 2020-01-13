#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//두 정수 x, y를 입력받아 x가 크면 1, y가 크면 0을 출력하는 프로그램을 작성하시오.
int main() {
	int x, y;
	printf("두 정수를 입력하시오\n");
	scanf("%d\n%d", &x, &y);
	printf("두 정수 %d > %d의 관계연산 결과 : %d \n",x,y,(x>y? 1:0));
}