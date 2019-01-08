class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        minCost_2StairBefore,minCost_1StairBefore = 0,0

        for x in cost:
            minCost_2StairBefore,minCost_1StairBefore = \
            minCost_1StairBefore,min(minCost_2StairBefore+x,minCost_1StairBefore+x)

        return min(minCost_2StairBefore,minCost_1StairBefore)
