#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    int suffix[numsSize];
    suffix[numsSize - 1] = 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        suffix[i] = suffix[i+1] * nums[i+1];
    }
    int *res = malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    res[0] = suffix[0];
    int prefix[numsSize];
    prefix[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        prefix[i] = prefix[i-1] * nums[i-1];
        res[i] = prefix[i] * suffix[i];
    }
    return res;
}