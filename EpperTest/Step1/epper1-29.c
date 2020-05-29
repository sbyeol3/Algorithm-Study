#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char samplePath[] = { "sample.txt" };
	int result = remove(samplePath);
	if (result==0) {
		printf("sample.txt를 삭제하였습니다.\n");
	}
	else if (result==-1) printf("파일 삭제에 실패했습니다.\n");
}