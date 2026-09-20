class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # sort by the first starting point
        output = [intervals[0]] # handling edge cases

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                # overlapped
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output

