var productExceptSelf = function(nums) {
    const suffix = new Array(nums.length);
    suffix[nums.length - 1] = 1;
    i = nums.length - 2;
    while (i >= 0) {
        suffix[i] = suffix[i+1] * nums[i+1];
        i--;
    }
    prefix = [1];
    res = [suffix[0]];
    i = 1;
    while (i < nums.length) {
        prefix.push(prefix[i-1] * nums[i-1]);
        res.push(prefix[i] * suffix[i]);
        i++;
    }
    return res;
};