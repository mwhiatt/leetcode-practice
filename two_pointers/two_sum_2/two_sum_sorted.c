#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    *returnSize = 2;
    int start = 0;
    int end = numbersSize -1;
    int *res = malloc(2 * sizeof(int));
    while (start < end) {
        int curr = numbers[start] + numbers[end];
        if (curr == target) {
            res[0] = start + 1;
            res[1] = end + 1;
            return res;
        }

        if (curr > target) {
            end--;
        } else {
            start++;
        }
    }
    return res;
}