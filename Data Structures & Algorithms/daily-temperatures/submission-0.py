class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures), 1):
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break

        return output
                    