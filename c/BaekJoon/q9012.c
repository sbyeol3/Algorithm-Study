#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int top = -1; // stack top�� index

void Push(char* stack) { // '('�� stack�� push
	stack[++top] = '(';
}


int VPS(char* X) { // �ϳ��� �׽�Ʈ���̽� result �Ǵ�
	char stack[51];
	top = -1;

	int isVPS = 1;
	for (int i = 0; X[i]; i++) {
		if (X[i] == '(')
			Push(stack);
		else {
			if (top == -1) {
				isVPS = 0;
				break;
			}
			else top--;
		}
	}

	if (isVPS == 1 && top != -1) isVPS = 0;
	return isVPS;
}

int main() {
	int isVPS[10000];
	int T, i;
	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		char str[51];
		scanf("%s", str);
		isVPS[i] = VPS(str);
	}

	for (i = 0; i < T; i++) // ��� ���
		isVPS[i] == 1 ? printf("YES\n") : printf("NO\n");
}