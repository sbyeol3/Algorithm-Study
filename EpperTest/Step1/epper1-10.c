#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 두 정수를 입력받아 AND OR XOR Complement 비트연산을 수행하는 프로그램을 작성하라.
int main() {
	int x, y;
	printf("두 정수를 입력하시오\n");
	scanf("%d\n%d", &x, &y);
	printf("%d & %d = %d\n",x,y,x&y);
	printf("%d | %d = %d\n",x,y,x|y);
	printf("%d ^ %d = %d\n",x,y,x^y);
	printf("~%d = %d\n",x,~x);
	printf("~%d = %d\n",y,~y);
	printf("<~%d> + 1= %d\n",x,(~x+1));
	printf("<~%d> + 1= %d\n",y,(~y+1));
	return 0;
}