#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set;
        for (int i : nums) {
            set.insert(i);
        }
        int longest = 0;
        for (int i : set) {
            if (set.count(i-1) != 1) {
                int length = 1;
                while (set.count(i+length) == 1) {
                    length++;
                }
                if (length > longest) {
                    longest = length;
                }
            }
        }
        return longest;
    }
};