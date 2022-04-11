#import List
class Solution:
    def fizzBuzz(self, n: int):
        result = []
        for tmp in range(1, n+1):
            if tmp % 3 == 0 and tmp % 5 == 0:
                result.append("FizzBuzz")
            elif tmp % 3 == 0:
                result.append("Fizz")
            elif tmp % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(tmp))
        return result

Solution().fizzBuzz(10)