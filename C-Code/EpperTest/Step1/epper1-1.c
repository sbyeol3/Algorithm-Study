#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char name[10];
	int height;
	printf("Enter your name:");
	scanf("%s", name);
	printf("Enter your height in cm:");
	scanf("%d", &height);
	printf("%s, your height is %.2fm.\n", name,(float)height / 100);
}
