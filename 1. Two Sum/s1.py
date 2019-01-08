class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result =[]
        size = len(nums)
        
        for i in range(0, size):
            for j in range(size-1, i, -1):
                #print ("[#",i,"+ #",j,"] = [",nums[i]," + ",nums[j],"]=[",nums[i]+nums[j],"]")
                if nums[i] + nums[j] == target:                                        
                   # print ("target sum ",target ," is find")
                    result = [i,j]
                    break
            else:
                continue
            break
        return result
        
