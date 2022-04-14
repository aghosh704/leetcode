from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        z_str = list(zip(*strs))

        for tmp in z_str:
            if all(v == tmp[0] for v in tmp):
                prefix.append(str(tmp[0]))
            else:
                break
        return ''.join(prefix)





x = Solution().longestCommonPrefix(["flo","flower","flag"])
print(x)

