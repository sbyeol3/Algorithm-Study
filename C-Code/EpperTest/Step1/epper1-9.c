#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// �� ������ �Է¹ް� ���ǿ�����( ? : )�� �̿��Ͽ�  �� ū ���� ����ϴ� ���α׷��� �ۼ��Ͽ���.
int main() {
	int x, y;
	printf("�� ������ �Է��Ͻÿ�\n");
	scanf("%d\n%d", &x, &y);
	printf("�� �� <%d, %d> �߿��� ū �� : %d \n", x, y, (x > y ? x : y));
}