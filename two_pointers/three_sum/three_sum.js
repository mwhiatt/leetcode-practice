/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  res = [];
  nums.sort((a,b) => a-b)

  for (let i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
          break;
      }
      if (i > 0 && (nums[i] == nums[i-1])) {
          continue;
      }

      l = i+1;
      r = nums.length - 1;
      while (l < r) {
          sum = nums[i] + nums[l] + nums[r]
          if (sum < 0) {
              l++;
          } else if (sum > 0) {
              r--;
          } else {
              res.push([nums[i], nums[l], nums[r]])
              l++;
              r--;
              while (l < r && (nums[l] === nums[l-1])) {
                  l++;
              }
          }
      }
  }

  return res;
};