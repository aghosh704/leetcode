class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        nums = []
        while x > 0:

            nums.append(x % 10)
            x = int(x / 10)

        factor = pow(10, len(nums)-1)
        reversed_num = 0
        for tmp in nums:
            reversed_num += int(factor * tmp)
            factor /= 10

        reversed_num *= sign
        
        return reversed_num if -pow(2, -31) < reversed_num <= pow(2, 31) - 1 else 0

print(Solution().reverse(-123))