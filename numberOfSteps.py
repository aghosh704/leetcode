class Solution:
    def numberOfSteps(self, num: int) -> int:
        cntr = 0
        while num != 0:

            cntr += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
        return cntr

print(Solution().numberOfSteps(14))