#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
//물건의 가격과 지불한 돈의 액수를 입력해 거스름돈으로 받을 화폐의 종류와 개수를 출력하세요.

int main() {
	int price, cost;
	int money[] = { 10000,5000,1000,100,50,10 };
	int num[6] = { 0, };

	printf("물건의 가격 : "); scanf("%d", &price);
	printf("지불한 금액 : "); scanf("%d", &cost);

	int change = cost - price;
	for (int i = 0; i < 6; i++)
		while (change >= money[i]) {
			num[i]++;
			change -= money[i];
		}

	for (int i = 0; i < 6; i++)
		if (num[i] != 0) printf("%d원 : %d\n", money[i], num[i]);
}