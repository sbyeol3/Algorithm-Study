#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// main 함수에서 사용자로부터 두 정수를 입력 받고,
// 포인터를 인자로 보내서 변수 두 개의 값을 바꾸는 함수를 작성하라.

void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

int main() {
	int* a, * b;
	printf("두 정수를 입력하시오\n");
	scanf("%d", &a); scanf("%d", &b);
	
	printf("a=%d b=%d\n", a, b);
	swap(&a, &b);
	printf("a=%d b=%d\n", a, b);
	return 0;
}