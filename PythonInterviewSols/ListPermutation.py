def ListPerm(nums):

  if len(nums)==0:
    return []
  if len(nums)==1:
    return [nums]

  l=[]
  for i in range(len(nums)):
    first=nums[i]
    notused=nums[:i]+nums[i+1:]

    for p in ListPerm(notused):
      print(p)
      l.append([first]+p)
  return l
print(ListPerm([1,2,3]))