#Leetcode 529 - Mine Sweeper

#define map = [][]
#define max_row
#define max_col
#define open_cell(map, row, col): update cell[row,col] in map, update nothing if invalid value (out of boundary) selected
#define count_mine(map, row, col): count no. of adjacenet mines in cell[row,col], and update the count in map


#************************************************************

#int count_mine(map,[row][col])
count = 0
if (row-1) > 0
	if (col-1>0): if map[row-1][col-1] == 'M': count+=1
	if map[row-1][col] == 'M': count+=1
	if (col+1<max_col): if map[row-1][col+1] == 'M': count+=1

if (col-1>0): if map[row][col-1] == 'M': count+=1
if (col+1<max_col): if map[row][col+1] == 'M': count+=1

if (row+1) <max_row
	if (col-1>0): if map[row+1][col-1] == 'M': count+=1
	if map[row+1][col] == 'M': count+=1
	if (col+1<max_col): if map[row+1][col+1] == 'M': count+=1

return count

#************************************************************

#map open_cell (map, [row][col])

if 	(row-1) > 0 or\
	(row+1<max_row) or \
	(col-1) > 0 or \
	(col+1<max_col): 
return map


if map(row,col) == 'M'	
	return map	#end game

if map(row,col)  == 'E'

	count_mine(row,col)

	open_cell(map, [row-1][col-1])
	open_cell(map, [row-1][col])
	open_cell(map, [row-1][col+1])

	open_cell(map, [row][col-1])
	open_cell(map, [row][col+1])

	open_cell(map, [row+1][col-1])
	open_cell(map, [row+1][col])
	open_cell(map, [row+1][col+1])

	return map	#end game
#************************************************************
