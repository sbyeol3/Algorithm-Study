#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//사용자로부터 두 정수를 입력 받아 거듭 제곱 값을 구하는 프로그램을 작성하시오
// 이 때 사용자로부터 정수를 입력 받는 함수 int get_ingeter(void)와
// 거듭제곱 값을 구하는 함수 int power(int x, int y)를 만들어 사용할 것.

int get_integer(void) {
	int num;
	printf("정수를 입력하시오 : ");
	scanf("%d", &num);
	return num;
}

int power(int x, int y) {
	int num = 1;
	while (y-- > 0)
		num *= x;
	return num;
}

int main() {
	int num1 = get_integer();
	int num2 = get_integer();
	int result = power(num1, num2);
	printf("%d의 %d승은 %d입니다.\n", num1, num2, result);
}