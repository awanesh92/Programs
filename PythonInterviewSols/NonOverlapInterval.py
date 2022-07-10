class Solution(object):
  def merge(self, intervals):
    if len(intervals) == 0:
      return []

    intervals = sorted(intervals, key=lambda k:k[0])

    out = [intervals[0]]
    for i in range(1, len(intervals)):
      if intervals[i][0] <= out[-1][1]:
        out[-1][1] = max(out[-1][1], intervals[i][1])
      else:
        out.append(intervals[i])

    return out

s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))