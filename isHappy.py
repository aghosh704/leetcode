"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

"""
class Solution:
    def digits(self, n):
        digits = []
        for i in str(n):
            digits.append(int(i))
        return digits

    def isHappy(self, n: int) -> bool:

        dig_map = {}
        cnt = 0
        tmp = n
        while True:
            digs = self.digits(tmp)
            from functools import reduce
            digs_sqr = list(map(lambda x: x*x, digs))
            tmp = reduce(lambda x, y: x + y, digs_sqr)
            if tmp == 1:
                return True
            if tmp in dig_map:
                return False
            else:
                dig_map[tmp] = 1
            cnt += 1


print(Solution().isHappy(19))