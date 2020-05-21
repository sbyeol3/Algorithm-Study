#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char name[100];
	char* addr[100];

	printf("이름을 입력하시오 : ");
	gets(name);
	printf("주소를 입력하시오 : ");
	gets(addr);
		
	printf("이름 : ");
	puts(name);
	printf("주소 : ");
	puts(addr);
}