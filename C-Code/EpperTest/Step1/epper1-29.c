#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char samplePath[] = { "sample.txt" };
	int result = remove(samplePath);
	if (result==0) {
		printf("sample.txt�� �����Ͽ����ϴ�.\n");
	}
	else if (result==-1) printf("���� ������ �����߽��ϴ�.\n");
}