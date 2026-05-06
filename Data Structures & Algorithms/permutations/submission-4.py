class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        output = []
        sub_results = self.permute(nums[1:])
        for res in sub_results:
            for i in range(len(res) + 1):
                res_copy = res.copy()
                res_copy.insert(i, nums[0])
                output.append(res_copy)
        return output
            


            
            
