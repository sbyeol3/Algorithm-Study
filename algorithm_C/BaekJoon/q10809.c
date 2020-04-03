#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int location[26], i;
	char s[100];
	scanf("%s", s);
	int length = strlen(s);

	for (i = 0; i < 26; i++) location[i] = -1;
	for (i = 0; i < length; i++)
		if (location[s[i] - 97] == -1) location[s[i] - 97] = i;

	for (i = 0; i < 26; i++) printf("%d ", location[i]);
	putchar('\n');
}