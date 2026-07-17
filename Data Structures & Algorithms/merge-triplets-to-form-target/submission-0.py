class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        valid = []

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                valid.append(triplet)

        for idx in range(len(target)):
            is_present = set([triplet[idx] for triplet in valid])
            if target[idx] not in is_present:
                return False
        
        return True

                    

