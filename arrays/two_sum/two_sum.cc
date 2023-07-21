#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prev;
        vector<int> result;
        for (int i=0; i<nums.size(); i++) {
            if (prev.find(target-nums[i]) != prev.end()) {
                result = {prev[target-nums[i]], i};
                return result;
            }
            prev[nums[i]] = i;
        }
        result = {0, 1};
        return result;
    }
};