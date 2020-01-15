#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct Student
{
	int id;
	char name[20];
	double grade;
};

int main() {
	struct Student stds[3] = { { 1,"kim",3.99 },{ 2,"min",2.68 }, { 3,"lee",4.01 } };
	struct Student s; // read를 위한 구조체 변수

	FILE* fp = fopen("grade.dat", "wb");
	fwrite(stds, sizeof(struct Student), 3, fp);
	fclose(fp);

	fp = fopen("grade.dat", "rb");
	while (1) {
		fread(&s, sizeof(s),1, fp);
		if (feof(fp)) break;
		printf("학번 : %d / 이름 : %s / 평점 : %.5f\n", s.id,s.name,s.grade);
	}

	fclose(fp);
	return 0;
}