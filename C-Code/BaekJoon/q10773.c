#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int stack[100000];
int topIndex = -1;
int sum = 0;

void Push(int X) {
	stack[++topIndex] = X;
	sum += X;
}

void Pop() {
	if (topIndex == -1) return;
	else if (topIndex == 0) {
		sum = 0;
		topIndex--;
	}
	else {
		sum -= stack[topIndex];
		topIndex--;
	}
}

int main() {
	int K, N;
	scanf("%d", &K);
	while (K-- > 0) {
		scanf("%d", &N);
		if (N == 0) Pop();
		else Push(N);
	}

	printf("%d\n", sum);
}