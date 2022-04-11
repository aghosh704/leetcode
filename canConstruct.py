class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}
        for tmp in magazine:
            magazine_map[tmp] = magazine_map.get(tmp, 0) + 1

        for tmp in ransomNote:
            cnt = magazine_map.get(tmp, 0)
            if cnt == 0:
                return False
            else:
                magazine_map[tmp] = cnt - 1
        return True

print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))
