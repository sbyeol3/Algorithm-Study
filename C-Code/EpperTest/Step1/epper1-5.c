#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {
	int a, b, c;
	float sol1, sol2;

	printf("ax^2+bx+c ���� ���������� ����� �Է��ϼ���\n");
	printf("a : ");  scanf("%d", &a);
	printf("b : ");  scanf("%d", &b);
	printf("c : ");  scanf("%d", &c);

	sol1 = (-b + sqrt(b * b - 4 * a * c)) / 2.0 * a;
	sol2 = (-b - sqrt(b * b - 4 * a * c)) / 2.0 * a;
	printf("���������� %dx^2+%dx+%d�� �� ���� %f, %f�Դϴ�.\n", a, b, c, sol1,sol2);
}