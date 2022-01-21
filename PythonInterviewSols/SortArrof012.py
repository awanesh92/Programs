def sortArry(arr):
  left,right=0,len(arr)-1
  i=0
  while i<right:#traverse till the right pointer as after that pointer it will be already sorted with value2
    if arr[i]==0:
      arr[i],arr[left]=arr[left],arr[i]
      left+=1
    if arr[i]==2:
      arr[i],arr[right]=arr[right],arr[i]
      right-=1
      i-=1#decrement i pointer as it may again contain value that we might need to replace
    i+=1

  return arr

assert [0,0,0,1,1,1,2,2]==sortArry([1, 2, 0, 1, 1, 0, 2, 0])