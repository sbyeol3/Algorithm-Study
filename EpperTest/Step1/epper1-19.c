#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
//������ ���ݰ� ������ ���� �׼��� �Է��� �Ž��������� ���� ȭ���� ������ ������ ����ϼ���.

int main() {
	int price, cost;
	int money[] = { 10000,5000,1000,100,50,10 };
	int num[6] = { 0, };

	printf("������ ���� : "); scanf("%d", &price);
	printf("������ �ݾ� : "); scanf("%d", &cost);

	int change = cost - price;
	for (int i = 0; i < 6; i++)
		while (change >= money[i]) {
			num[i]++;
			change -= money[i];
		}

	for (int i = 0; i < 6; i++)
		if (num[i] != 0) printf("%d�� : %d\n", money[i], num[i]);
}