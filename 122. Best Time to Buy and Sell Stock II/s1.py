class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        isBuying = True
        earning = 0
    
        if (len(prices)>1):
            if (prices[1]>prices[0]):
                earning-= prices[0]
                isBuying = False
                #print("buy at: $",prices[0], ", balance: $",earning)
            
        for i in range(1, len(prices)):         
            if (isBuying):
                if (prices[i] > prices[i-1]):
                    earning-= prices[i-1]
                    isBuying = False
                    #print("buy at: $",prices[i-1], ", balance: $",earning)
            elif (prices[i] < prices[i-1]):
                    earning+= prices[i-1]
                    isBuying = True
                    #print("sell at: $",prices[i-1], ", balance: $",earning)
                
        if (not isBuying):
            earning+= prices[len(prices)-1]            
            #print("sell at: $",prices[len(prices)-1], ", balance: $",earning)
        
        
        #print("total earning: $",earning)
        
        
        
        
        return earning
