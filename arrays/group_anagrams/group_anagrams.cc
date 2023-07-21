#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict; //same as python but key is string instead of tuple
        //build dictionary
        for (string s : strs) {
            string key = getKey(s);
            dict[key].push_back(s);
        }

        //get values
        vector<vector<string>> res;
        for (auto it = dict.begin(); it != dict.end(); it++) {
            res.push_back(it->second);
        }
        return res;
    }

    string getKey(string s) {
        vector<int> count(26);
        for (char c : s) {
            count[c-'a']+=1;
        }

        string key = "";
        for (int i : count) {
            key.append(to_string(i+'a'));
        }
        return key;
    }
};