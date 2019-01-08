import itertools

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # https://leetcode.com/problems/house-robber/discuss/55977/Python-DP-solution-4-line-O(n)-time-O(1)-space-easy-to-understand-with-detailed-explanation
                       
        max_earning__three_house_before,  max_earning__two_house_before, adjacent_house = 0,0,0         
        
        for index, x in enumerate(nums):
            """
            print ("\t ",max_earning__three_house_before,\
                   " ",max_earning__two_house_before,\
                   " ",adjacent_house,\
                   " ",x\
                  )   
            """      
            max_earning__three_house_before,max_earning__two_house_before, adjacent_house= \
            max_earning__two_house_before,\
            adjacent_house,\
            max(max_earning__three_house_before + x, max_earning__two_house_before+x)
            
        
        #print("max_earning: $",max(max_earning__two_house_before, adjacent_house))
        return max(max_earning__two_house_before, adjacent_house)
