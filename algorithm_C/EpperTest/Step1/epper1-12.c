#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int year, month;
	int leapYear = 0;
	int days[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	printf("������ ���� �Է��ϼ��� >> ");
	scanf("%d %d", &year, &month);
	
	if (year % 400 == 0) leapYear = 1;
	else if (year % 4 == 0 && year % 100 != 0) leapYear = 1;
	if (leapYear == 1) days[1] = 29;

	printf("%d���� ", year);
	leapYear == 0 ? printf("���") : printf("����");
	printf("�̰� %d�� %d���� %d���Դϴ�.\n", year, month, days[month - 1]);
}