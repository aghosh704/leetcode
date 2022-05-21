"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover
all the intervals in the input.
"""
class Solution:
    from typing import List

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        curr = intervals[0]
        for idx in range(len(intervals)):
            curr_start = curr[0]
            curr_stop = curr[1]
            next_start = intervals[idx][0]
            next_stop = intervals[idx][1]
            if next_start <= curr_stop:  # merge
                tmp = [min(curr_start, next_start), max(next_stop, curr_stop)]
                curr = tmp
            else:
                merged_intervals.append(curr)
                curr = intervals[idx]
        merged_intervals.append(curr)
        return merged_intervals


arr = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(Solution().merge(arr))