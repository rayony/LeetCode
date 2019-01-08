class Solution:
    
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #init dict using J
        dict = {}          
        for i in range(len(J)):
            dict[J[i]]=S.count(J[i])         
        
        #update count by summing up the dict        
        count =sum(dict.values())         
        
        return count
