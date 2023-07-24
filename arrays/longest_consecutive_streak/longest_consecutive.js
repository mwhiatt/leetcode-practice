/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
  const uniques = new Set(nums);
  let longest = 0;

  for (const num of uniques) {
      if (!uniques.has(num-1)) {
          length = 1;
          while (uniques.has(num+length)) {
              length++;
          }
          if (length > longest) longest = length;
      }
  }
  return longest;
};