#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char name[100];
	char* addr[100];

	printf("�̸��� �Է��Ͻÿ� : ");
	gets(name);
	printf("�ּҸ� �Է��Ͻÿ� : ");
	gets(addr);
		
	printf("�̸� : ");
	puts(name);
	printf("�ּ� : ");
	puts(addr);
}