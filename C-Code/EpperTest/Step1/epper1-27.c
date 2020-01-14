#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int year, half;
	float radiation = 100;
	printf("초기 방사능량 : 100\n");
	printf("반감기(년)을 입력하세요 : ");
	scanf("%d", &year);
	half = year;

	while (radiation > 10) {
		radiation /= 2;
		printf("%d년 후에 남은 양 : %.3f\n", year, radiation);
		year += half;
	}
	printf("1/10 이하까지 걸린 시간 : %d년\n", year-half);
}