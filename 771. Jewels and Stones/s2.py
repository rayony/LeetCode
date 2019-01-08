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
            dict[J[i]]=0
        
        #update count by comparing dict and S
        for i in range(len(S)):
            if S[i] in dict:
                dict[S[i]]+=1                
        
        #update count by summing up the dict        
        count =sum(dict.values())         
        
        return count
