#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//�� ���� x, y�� �Է¹޾� x�� ũ�� 1, y�� ũ�� 0�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main() {
	int x, y;
	printf("�� ������ �Է��Ͻÿ�\n");
	scanf("%d\n%d", &x, &y);
	printf("�� ���� %d > %d�� ���迬�� ��� : %d \n",x,y,(x>y? 1:0));
}