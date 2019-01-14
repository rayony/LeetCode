#Leetcode 529 - Mine Sweeper
#https://leetcode.com/problems/minesweeper/

class Solution:
    #ensure global variable is initialized for each test case in LeetCode.
    def __init__(self):
        self.isVisited = {}        

#************************************************************
    #check if selected cell board[r][c] is within boundary
    def isValidAddr(self,board,r,c):

        if 0<=r<len(board) and 0<=c<len(board[0]):
            return True
        else:
            return False

#************************************************************
    #count and return the no. of adjacent mines in the selected cell
    def countMine(self, board, click):
        
        row = click[0]
        col = click[1]
        count = 0

        for r in [row-1,row,row+1]:
            for c in [col-1,col,col+1]:
                if (self.isValidAddr(board, r,c)):
                    if board[r][c] == 'M':
                        count+=1

        return str(count)

#************************************************************    
    #update answer w.r.t selected cell
    def updateAnswer(self, ans, click):

        row = click[0]
        col = click[1]

        #case 1: no need update if selected cell already updated, else mark visited
        if (row,col) in self.isVisited:
            return ans
        else:
            self.isVisited[(row,col)]=True

        #case 2: if the selected cell is 'M', mark it as 'X'
        if ans[row][col] == 'M':
            ans[row][col] = 'X'
            return ans

        #case 3: if the selected cell is 'E', count the no. of mines around the selected cell, reveal surrounding cells if count = 0
        if ans[row][col] == 'E':
            ans[row][col] = self.countMine(ans, (row,col))

            if (ans[row][col]=='0'):
                ans[row][col]='B'
                for r in [row-1,row,row+1]:
                    for c in [col-1,col,col+1]:
                        if self.isValidAddr(ans, r,c):
                            self.updateBoard(ans, (r,c))
                            
            return ans

        #default: exception
        print("Error: ",ans[row][col]," at [",row,",",col,"]")
        return ans

#************************************************************
    #dummy function caller
    def updateBoard(self, board, click):
        answer = board.copy()
        return self.updateAnswer(answer,click)

#************************************************************
