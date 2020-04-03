#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>	
#include <stdlib.h> // 동적할당
// N개의 서로 다른 자연수가 주어질 때, 이들 중 최대값을 출력하고
// 몇 번째 숫자인지 출력하는 프로그램을 작성하세요.

int main() {
	int N, pos=0;
	int* num;

	printf("N : "); scanf("%d", &N);
	num = (int *)malloc(sizeof(int)* N);
	printf("자연수 입력 : ");

	for(int i=0;i<N;i++)
		scanf("%d", &num[i]);

	int max = num[0];
	for (int i = 1; i < N; i++)
		if (max < num[i]) {
			max = num[i];
			pos = i;
		}

	printf("최대값은 %d, %d번째에 위치\n", max, pos);
	free(num);
}