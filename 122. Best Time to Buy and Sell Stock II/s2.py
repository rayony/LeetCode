class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """                
        earning = 0
        
        if (len(prices) <1):
            return 0
        
        for i in range(1, len(prices)):            
            if (prices[i] > prices[i-1]):
                earning = earning + prices[i] - prices[i-1]
        
        #print("total earning: $",earning)
        
        return earning
