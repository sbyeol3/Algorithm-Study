#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// ���� 5���� ���� �� �� �ִ� �迭�� �����ϰ� ����ڷκ��� ������ 5�� �Է� ���� �� �����͸� ����Ͽ� �� ���� ���ϴ� ���α׷��� �ۼ��϶�.

int main() {
	int num[5];
	int i = 1, sum = 0;
	while (i < 6) {
		printf("���� %d : ", i);
		scanf("%d", &num[i - 1]);
		sum += num[i-1];
		i++;
	}
	printf("���� : %d\n", sum);
}