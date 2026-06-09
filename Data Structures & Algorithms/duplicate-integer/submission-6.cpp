#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> dupes;

        for (int element : nums) {
            if (!dupes.insert(element).second) {
                return true;
            }
        }
        return false;
    }
};