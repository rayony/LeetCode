#Leetcode 529 - Mine Sweeper
class Solution:

#define board = [][]

#************************************************************	
    def countMine(self, board, click):
    	#count and return the no. of adjacent mines in the selected cell
    	"""
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: integer
        """

        max_row = len(board)
        max_col = len(board[0])
        row = click[0]
        col = click[1]

		count = 0
		if (row-1) > 0:
			if (col-1>0) and board[row-1][col-1] == 'M': count+=1
			if board[row-1][col] == 'M': count+=1
			if (col+1<max_col) and board[row-1][col+1] == 'M': count+=1

		if (col-1>0) and board[row][col-1] == 'M': count+=1
		if (col+1<max_col) and board[row][col+1] == 'M': count+=1

		if (row+1) <max_row:
			if (col-1>0) and board[row+1][col-1] == 'M': count+=1
			if board[row+1][col] == 'M': count+=1
			if (col+1<max_col) and board[row+1][col+1] == 'M': count+=1

		return count


#************************************************************	
    def updateBoard(self, board, click):
    	#update board w.r.t selected cell, update nothing if invalid cell (out of boundary) selected
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        max_row = len(board)
        max_col = len(board[0])
        row = click[0]
        col = click[1]


        #case 1: update nothing if selected cell out of boundary
		if 	(row-1) > 0 or\
			(row+1<max_row) or \
			(col-1) > 0 or \
			(col+1<max_col): 
			return board

		#case 2: if selected cell is 'M', masking for unrevealed mines
		if board[row,col] == 'M':	
			#ToDo - update 'B' for mines in board other than board[row,col]
			return board

		#case 3: if selected cell is 'E', count the no. of mines in selected cell, reveal surrounding cells if count = 0
		if board[row,col]  == 'E':

			board[row,col] = self.countMine(board, row,col)

			if (board[row,col]==0):
				board[row,col]='B'
				self.updateBoard(board, (row-1,col-1))
				self.updateBoard(board, (row-1,col))
				self.updateBoard(board, (row-1,col+1))

				self.updateBoard(board, (row,col-1))
				self.updateBoard(board, (row,col+1))

				self.updateBoard(board, (row+1,col-1))
				self.updateBoard(board, (row+1,col))
				self.updateBoard(board, (row+1,col+1))

			return board

		#case: exception
		print("Error")
		return board
#************************************************************
