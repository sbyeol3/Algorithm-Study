#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {
	int a, b, c;
	float sol1, sol2;

	printf("ax^2+bx+c 꼴의 이차방정식 계수를 입력하세요\n");
	printf("a : ");  scanf("%d", &a);
	printf("b : ");  scanf("%d", &b);
	printf("c : ");  scanf("%d", &c);

	sol1 = (-b + sqrt(b * b - 4 * a * c)) / 2.0 * a;
	sol2 = (-b - sqrt(b * b - 4 * a * c)) / 2.0 * a;
	printf("이차방정식 %dx^2+%dx+%d의 두 근은 %f, %f입니다.\n", a, b, c, sol1,sol2);
}