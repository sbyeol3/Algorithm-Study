#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// ���ڿ��� �Է¹��� ��, �Է¹��� ���ڿ����� 
// ���ĺ� �ҹ���, ���ĺ� �빮��, ����, ��ȣ�� ������ ��� ����ϴ� ���α׷��� �ۼ��ϼ���.

int main() {
	char str[100];
	int upper=0, lower=0, num=0, mark=0;
	printf("���ڿ��� �Է��ϼ��� : ");
	scanf("%[^\n]s", str);

	for (int i = 0; i < strlen(str); i++) { // �ƽ�Ű�ڵ� �̿�
		if ('A' <= str[i] && str[i] <= 'Z') upper++;
		else if ('a' <= str[i] && str[i] <= 'z') lower++;
		else if ('0' <= str[i] && str[i] <= '9') num++;
		else if (33 <= str[i] && str[i] <= 126) mark++;
	}
	printf("�빮�� : %d\n", upper);
	printf("�ҹ��� : %d\n", lower);
	printf("���� : %d\n", num);
	printf("��ȣ : %d\n", mark);
}