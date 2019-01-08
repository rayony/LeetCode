class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """                
        #find greatest increase in given list

        #invalid input
        if (len(prices)<2):
            return 0
        
        #init              
        min_value = max(prices)
        max_earning = 0

        #iterate
        for x in prices:
            #print(x,min_value,max_earning)
            max_earning =  max(max_earning,x - min_value)
            min_value = min(min_value,x)

        #result
        #print(x,min_value,max_earning)
        return max_earning
