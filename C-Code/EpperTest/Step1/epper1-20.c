#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
#include <stdlib.h> // �����Ҵ�
// N���� ���� �ٸ� �ڿ����� �־��� ��, �̵� �� �ִ밪�� ����ϰ�
// �� ��° �������� ����ϴ� ���α׷��� �ۼ��ϼ���.

int main() {
	int N, pos=0;
	int* num;

	printf("N : "); scanf("%d", &N);
	num = (int *)malloc(sizeof(int)* N);
	printf("�ڿ��� �Է� : ");

	for(int i=0;i<N;i++)
		scanf("%d", &num[i]);

	int max = num[0];
	for (int i = 1; i < N; i++)
		if (max < num[i]) {
			max = num[i];
			pos = i;
		}

	printf("�ִ밪�� %d, %d��°�� ��ġ\n", max, pos);
	free(num);
}