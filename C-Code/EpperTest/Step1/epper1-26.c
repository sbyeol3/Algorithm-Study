#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char sample[100];
	FILE* fp = NULL;
	fp = fopen("sample.txt", "r");
	if (fp != NULL) {
		printf("���Ͽ��� ����\n");
		fgets(sample, sizeof(sample), fp);
		printf("%s\n", sample);
		fclose(fp);
	}
	else printf("���Ͽ��� ����\n");
}