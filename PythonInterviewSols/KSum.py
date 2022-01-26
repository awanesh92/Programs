from typing import List
class Solution:
  def kSum(self,k, nums: List[int], target, l=0):
    n=len(nums)
    result=[]
    if k<2:
      return
    elif k==2:
      return self.twoSum(nums,target,l)
    for i in range(l,n-k+1):
      if i>l and nums[i]==nums[i-1]:
        continue
      k_sum=self.kSum(k-1, nums, target-nums[i],l=i+1)
      for kp in k_sum:
        result.append([nums[i]]+kp)
    return result

  def twoSum(self, nums: List[int], target, l=0):
    n=len(nums)
    r=n-1
    result=[]
    while l<r:
      twosum=nums[l]+nums[r]
      if twosum < target:
        l+=1
      elif twosum > target:
        r-=1
      else:
        result.append([nums[l],nums[r]])
        while l<r and nums[l]==nums[l+1]:
          l+=1
        while l<r and nums[r]==nums[r-1]:
          r-=1
        l+=1
        r-=1
    return result
s=Solution()
nums=[1,0,-1,0,-2,2]
nums.sort()
print(s.kSum(4,nums,0))
