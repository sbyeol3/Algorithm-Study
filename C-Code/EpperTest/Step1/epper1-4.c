#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int height, IQ, EQ;
	double weight;
	char blood;

	printf("Ű:"); scanf("%d", &height);
	printf("IQ <8������ �Է�>:"); scanf("%o", &IQ);
	printf("EQ <16������ �Է�>:"); scanf("%x", &EQ);
	printf("������ <�Ҽ��� �Ʒ� ��°�ڸ�����>:"); scanf("%lf", &weight);
	printf("������:"); scanf("\n%c", &blood);
	printf("===================================================\n");
	printf("Ű�� %d, IQ�� %d, EQ�� %d�̰� \n �����Դ� %lf, �������� %c�̴�.\n\n",height,IQ,EQ,weight,blood);
}

