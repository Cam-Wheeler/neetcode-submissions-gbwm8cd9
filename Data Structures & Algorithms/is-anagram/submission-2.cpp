#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for (char element : s) {
            s_map[element] += 1;
        }

        for (char element : t) {
            t_map[element] += 1;
        }

        return s_map == t_map;
    }
};
