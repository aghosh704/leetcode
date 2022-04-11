class Solution:
    def kWeakestRows(self, mat, k: int):
        result = []
        for idx, tmp in enumerate(mat):
            result.append( (idx, sum(tmp) ) )
        sorted_formation = sorted(result, key=lambda x: (x[1], x[0]))
        print(sorted_formation)
        return [tmp[0] for tmp in sorted_formation[0:k]]


mat = (
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]

)
print(Solution().kWeakestRows(mat, 3))