#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int repeat, num = 1;
	double pi = 0;
	printf("�ݺ�Ƚ���� �Է��ϼ��� : "); scanf("%d", &repeat);

	while (repeat-- > 0) {
		if (num % 4 == 1)
			pi += (4.0 / num);
		else pi -= (4.0 / num);
		num += 2;
	}
	printf("Pi : %lf\n",pi);
}