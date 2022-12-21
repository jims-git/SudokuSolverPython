
count = 0

board = [
        5,3,0,0,7,0,0,0,0,
        6,0,0,1,9,5,0,0,0,
        0,9,8,0,0,0,0,6,0,
        8,0,0,0,6,0,0,0,3,
        4,0,0,8,0,3,0,0,1,
        7,0,0,0,2,0,0,0,6,
        0,6,0,0,0,0,2,8,0,
        0,0,0,4,1,9,0,0,5,
        0,0,0,0,8,0,0,0,0
        ]  
#        0,0,0,0,8,0,0,7,9  # use this for 1 possible solution

def print_board() :
    global board

    for y in range(9):
        if y % 3 == 0 and y != 0:
            print("- - - -+- - - - + - - -")

        for x in range(9):
            if x % 3 == 0 and x != 0:
                print(" | ", end="")

            if x == 8:
                print(board[y*9+x])
            else:
                print(str(board[y*9+x]) + " ", end="")
    print()

def possible(y,x,n) :
	global board
	
    # Check if n is in row
	for i in range(0,9) :
		if board[y*9+i] == n :
			return False
	
    # Check if n is in column
	for i in range(0,9) :
		if board[i*9+x] == n :
			return False
	
    # Check if n is in square
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3) :
		for j in range(0,3) :
			if board[y0*9+i*9+x0+j] == n :
				return False
	# n is not in row, column or square at this point
	return True
	
def solve() :
    global count, grid
    for y in range(9) :
        for x in range(9) :
            if board[y*9+x] == 0 :
                for n in range(1,10) :
                    if possible(y, x, n) :
                        board[y*9+x] = n
                        solve()
                        board[y*9+x] = 0
                return
    # If we get to this point, then the grid is solved
    count += 1
    print(f"\nSolution # {count}")
    print_board()
    
# MAIN

print("\nStarting Board")
print_board()
solve()


"""

Starting Grid
5 3 0  | 0 7 0  | 0 0 0
6 0 0  | 1 9 5  | 0 0 0
0 9 8  | 0 0 0  | 0 6 0
- - - -+- - - - + - - -
8 0 0  | 0 6 0  | 0 0 3
4 0 0  | 8 0 3  | 0 0 1
7 0 0  | 0 2 0  | 0 0 6
- - - -+- - - - + - - -
0 6 0  | 0 0 0  | 2 8 0
0 0 0  | 4 1 9  | 0 0 5
0 0 0  | 0 8 0  | 0 0 0


Solution # 1
5 3 4  | 6 7 8  | 1 9 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - -+- - - - + - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 9 7 1
7 1 3  | 9 2 4  | 8 5 6
- - - -+- - - - + - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 7 1 9


Solution # 2
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - -+- - - - + - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - -+- - - - + - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9

"""