#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> dupes;

        for (int element : nums) {
            dupes.insert(element);
        }

        return dupes.size() != nums.size();
    }
};