const twoSum = function(nums, target) {
  const prev = new Map();
  for (let i = 0; i < nums.length; i++) {
      if (prev.has(target - nums[i])) {
          return [prev.get(target-nums[i]), i];
      }
      prev.set(nums[i], i);
  }
  return []
};