#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 0과 100 사이의 숫자를 입력받아 각 자릿수별로 몇개의 숫자가 입력되었는지 출력한다.
int main() {
	int num[10] = { 0, };
	int tmp = 0;
	printf("0과 100사이의 숫자를 입력하세요. (종료는 음수 입력)\n");
	
	while (tmp >= 0) {
		scanf("%d", &tmp);
		if (tmp > 0 && tmp < 100) num[tmp / 10]++;
		else if (tmp < 0) break;
		else printf("Input Error!\n");
	}

	for (int i = 0; i < 10; i++) 
		if (num[i] != 0)
			printf("%d ~ %d : %d개\n",i*10,i*10+9,num[i]);
}