#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int MIN = -1000000;
int MAX = 1000000;

void solution(int N) {
    char nums[30] = "20 10 35 30 7";
    char *ptr = strtok(nums, " ");
    int min = MAX, max = MIN;
    
    while (ptr != NULL) {
        int num = atoi(ptr);
        if (num > max) max = num;
        if (num < min) min = num;
        ptr = strtok(NULL, " ");
    }
    
    printf("%d %d\n",min,max);
};

int main() {
    solution(5);
};
