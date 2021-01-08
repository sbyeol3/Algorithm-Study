#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int stack[10000];
int* top;
int topIndex = -1;

void Push(int X) {
	stack[++topIndex] = X;
	top = &stack[topIndex];
}

int Pop() {
	if (topIndex == -1) return -1;
	else if (topIndex == 0) {
		top = NULL;
		return stack[topIndex--];
	}
	else {
		top = &stack[topIndex - 1];
		return stack[topIndex--];
	}
}


int main() {
	int N, X;
	char command[20];
	scanf("%d", &N);
	while (N-- > 0) {
		scanf("%s", command);
		if (strcmp(command, "push")==0) {
			scanf("%d", &X);
			Push(X);
		}
		else if (strcmp(command, "pop") == 0) printf("%d\n", Pop());
		else if (strcmp(command, "size") == 0)  
			topIndex == -1 ? printf("0\n") : printf("%d\n", topIndex+1);
		else if (strcmp(command, "empty") == 0) 
			topIndex == -1 ? printf("1\n") : printf("0\n");
		else if (strcmp(command, "top") == 0)	
			topIndex == -1 ? printf("-1\n") : printf("%d\n", stack[topIndex]);
	}
}