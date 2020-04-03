#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	

int main() {
	int num;
	int a = 0 , b= 0;

	printf("정수를 입력하세요 : ");
	scanf("%d", &num);

	for (int i = 1; i < num;i++) 
		for (int j=1;j<num;j++)
			if (i * i + j * j == num) {
				a = i;
				b = j;
				break;
			}	

	(a == 0 && b == 0) ? printf("조건을 만족하지 않는 수입니다.\n") : printf("%d = %d + %d 조건을 만족하는 수입니다.\n", num, a * a, b * b);
}