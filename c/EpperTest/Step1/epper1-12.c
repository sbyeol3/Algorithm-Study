#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int year, month;
	int leapYear = 0;
	int days[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	printf("연도와 월을 입력하세요 >> ");
	scanf("%d %d", &year, &month);
	
	if (year % 400 == 0) leapYear = 1;
	else if (year % 4 == 0 && year % 100 != 0) leapYear = 1;
	if (leapYear == 1) days[1] = 29;

	printf("%d년은 ", year);
	leapYear == 0 ? printf("평년") : printf("윤년");
	printf("이고 %d년 %d월은 %d일입니다.\n", year, month, days[month - 1]);
}