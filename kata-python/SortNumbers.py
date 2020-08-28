def solution(nums):
    pass
    if nums == None: 
        return []
    else: 
        return sorted(nums)
        
 #Seconda Soluzione
 
 #def solution(nums):  
  #  pass
  #  if nums == None:
  #      n = 0
  #      return []
  #  else:
  #      n = len(nums) 
  #  for i in range(n-1): 
  #      for j in range(0, n-i-1): 
  #          if nums[j] > nums[j+1] : 
  #              nums[j], nums[j+1] = nums[j+1], nums[j] 
  #  return nums