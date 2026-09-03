# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            current_guess = (l + r) // 2
            answer = guess(current_guess)
            if answer == 0:
                return current_guess
            elif answer > 0:
                l = current_guess + 1
            else:
                r = current_guess - 1
            
        return current_guess