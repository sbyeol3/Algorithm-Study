#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int height, IQ, EQ;
	double weight;
	char blood;

	printf("키:"); scanf("%d", &height);
	printf("IQ <8진수로 입력>:"); scanf("%o", &IQ);
	printf("EQ <16진수로 입력>:"); scanf("%x", &EQ);
	printf("몸무게 <소수점 아래 둘째자리까지>:"); scanf("%lf", &weight);
	printf("혈액형:"); scanf("\n%c", &blood);
	printf("===================================================\n");
	printf("키는 %d, IQ는 %d, EQ는 %d이고 \n 몸무게는 %lf, 혈액형은 %c이다.\n\n",height,IQ,EQ,weight,blood);
}

