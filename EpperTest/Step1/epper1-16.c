#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	

int main() {
	int num;
	int a = 0 , b= 0;

	printf("������ �Է��ϼ��� : ");
	scanf("%d", &num);

	for (int i = 1; i < num;i++) 
		for (int j=1;j<num;j++)
			if (i * i + j * j == num) {
				a = i;
				b = j;
				break;
			}	

	(a == 0 && b == 0) ? printf("������ �������� �ʴ� ���Դϴ�.\n") : printf("%d = %d + %d ������ �����ϴ� ���Դϴ�.\n", num, a * a, b * b);
}