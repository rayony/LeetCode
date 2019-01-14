#Leetcode 529 - Mine Sweeper
#https://leetcode.com/problems/minesweeper/

class Solution:

    isVisited = {}

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

        #print(row,col," =",count)
        return str(count)

#************************************************************    
    #update board w.r.t selected cell, update nothing if invalid cell (out of boundary) selected
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        row = click[0]
        col = click[1]

        #case 1: no need update if selected cell already updated, else mark visited
        if (row,col) in self.isVisited:
            return board
        else:
            self.isVisited[(row,col)]=True
        #print(self.isVisited)

        #case 2: if the selected cell is 'M', mark it as 'X'
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        #case 3: if the selected cell is 'E', count the no. of mines around the selected cell, reveal surrounding cells if count = 0
        if board[row][col] == 'E':
            board[row][col] = self.countMine(board, (row,col))
            if (board[row][col]=='0'):
                board[row][col]='B'
                for r in [row-1,row,row+1]:
                    for c in [col-1,col,col+1]:
                        #print("tmp",r,c)
                        if self.isValidAddr(board, r,c):
                            self.updateBoard(board, (r,c))
            return board

        #default: exception
        print("Error: ",board[row][col]," at [",row,",",col,"]")
        return board
#************************************************************
