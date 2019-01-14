#Leetcode 529 - Mine Sweeper
class Solution:

#define map = [][]
#define max_row
#define max_col
#define open_cell(map, row, col): update cell[row,col] in map, update nothing if invalid value (out of boundary) selected
#define count_mine(map, row, col): count no. of adjacent mines in cell[row,col], and update the count in map


#************************************************************
    def countMine(self, board, click):
    	"""
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: integer
        """
		count = 0
		if (row-1) > 0:
			if (col-1>0): if map[row-1][col-1] == 'M': count+=1
			if map[row-1][col] == 'M': count+=1
			if (col+1<max_col): if map[row-1][col+1] == 'M': count+=1

		if (col-1>0): if map[row][col-1] == 'M': count+=1
		if (col+1<max_col): if map[row][col+1] == 'M': count+=1

		if (row+1) <max_row:
			if (col-1>0): if map[row+1][col-1] == 'M': count+=1
			if map[row+1][col] == 'M': count+=1
			if (col+1<max_col): if map[row+1][col+1] == 'M': count+=1

		return count

#************************************************************
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        #case 1: update nothing if selected cell out of boundary
		if 	(row-1) > 0 or\
			(row+1<max_row) or \
			(col-1) > 0 or \
			(col+1<max_col): 
			return map

		#case 2: if selected cell is 'M', masking for unrevealed mines
		if map(row,col) == 'M':	
			#ToDo - update 'B' for mines in map other than map(row,col)
			return map

		#case 3: if selected cell is 'E', count the no. of mines in selected cell, reveal surrounding cells if count = 0
		if map(row,col)  == 'E':

			map(row,col) = self.countMine(map, row,col)

			if (map(row,col)==0):
				map(row,col)='B'
				self.updateBoard(map, [row-1][col-1])
				self.updateBoard(map, [row-1][col])
				self.updateBoard(map, [row-1][col+1])

				self.updateBoard(map, [row][col-1])
				self.updateBoard(map, [row][col+1])

				self.updateBoard(map, [row+1][col-1])
				self.updateBoard(map, [row+1][col])
				self.updateBoard(map, [row+1][col+1])

			return map

		#case: exception
		print("Error")
		return map
#************************************************************
