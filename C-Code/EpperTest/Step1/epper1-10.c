#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// �� ������ �Է¹޾� AND OR XOR Complement ��Ʈ������ �����ϴ� ���α׷��� �ۼ��϶�.
int main() {
	int x, y;
	printf("�� ������ �Է��Ͻÿ�\n");
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