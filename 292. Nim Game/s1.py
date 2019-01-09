class Solution:
    
    #define if A win score = 100, else A lose (i.e B wins) score = -100

    #define winning scenario for A's round (when player = A and remain = 1 to 3)    
    Turn_A_Score={
        1:100,
        2:100,
        3:100
    }
    
    #define winning scenario for B's round (when player = B and remain = 1 to 3)
    Turn_B_Score={
        1:-100,
        2:-100,
        3:-100
    }
    
    def  score(self,player,remain):

        if (player=='A'):
            #A is maximizing score in each round to give himself win, if remain >3;
            #N: max(TurnB(N-1),TurnB(N-2),TurnB(N-3))
            if remain not in self.Turn_A_Score:
                self.Turn_A_Score[remain] = max(self.score('B',remain-1),\
                                                self.score('B',remain-2),\
                                                self.score('B',remain-3))
            return self.Turn_A_Score[remain]

        else: #if (player=='B'):
            #B is minimizing score in each round to give himself win, if remain >3
            #N: min(TurnA(N-1),TurnA(N-2),TurnA(N-3))
            if remain not in self.Turn_B_Score:
                self.Turn_B_Score[remain] = min(self.score('A',remain-1),\
                                                self.score('A',remain-2),\
                                                self.score('A',remain-3))
            return self.Turn_B_Score[remain]       
    
    
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        #method 1: using math trick, which is essential for large no. if performance is required
        if (n > 1000000):
            return  n%4 != 0
                        
        #method 2: generic method using minimax tree
        if self.score('A', n) >= 100:
        	return True
        else:
	        return False
