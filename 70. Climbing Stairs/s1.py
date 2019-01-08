class Solution:
    
    dict = {0:0,1:1,2:2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n not in self.dict.keys():
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            #print("new dict: ",n," value = ",self.dict[n])
        return (self.dict[n])
        
