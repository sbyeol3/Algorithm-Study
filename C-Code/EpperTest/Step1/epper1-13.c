#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 0�� 100 ������ ���ڸ� �Է¹޾� �� �ڸ������� ��� ���ڰ� �ԷµǾ����� ����Ѵ�.
int main() {
	int num[10] = { 0, };
	int tmp = 0;
	printf("0�� 100������ ���ڸ� �Է��ϼ���. (����� ���� �Է�)\n");
	
	while (tmp >= 0) {
		scanf("%d", &tmp);
		if (tmp > 0 && tmp < 100) num[tmp / 10]++;
		else if (tmp < 0) break;
		else printf("Input Error!\n");
	}

	for (int i = 0; i < 10; i++) 
		if (num[i] != 0)
			printf("%d ~ %d : %d��\n",i*10,i*10+9,num[i]);
}