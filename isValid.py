class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        myq = deque()
        mymap = {'{': '}', '[': ']', '(': ')'}
        for tmp in s:
            if tmp in mymap:
                myq.append(tmp)
            else:
                if len(myq) == 0 or tmp != mymap[myq.pop()]:
                    return False
        return True if len(myq) == 0 else False

ans = Solution().isValid( "([]))")
print(ans)


