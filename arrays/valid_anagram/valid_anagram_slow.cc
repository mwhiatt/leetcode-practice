#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        for (char i : s) {
            if (t.find(i) == string::npos) {
                return false;
            }
            t.replace(t.find(i), 1, "");
        }
        return true;
    }
};