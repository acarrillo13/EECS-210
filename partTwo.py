#partTwo.py
def sudoku(grid, row, col):#the solver
    if row > 8:#checking to see if we are through the whole puzzle, becuase if we have moved to an index greater than eight it means that every space has been solved
        return True
    if grid[row][col] == '_':#checks for empty space
        for i in range(9):
            if check(grid, row, col, str(i+1)):
                grid[row][col] = str(i+1)
                if sudoku(grid, row, col):
                    return True
            grid[row][col] = '_'
    else:#if no empty space we move over to check the next index
        if col < 8:#if we are not at the end of a row we just add one to our col
            return sudoku(grid, row, col+1)
        elif col == 8:#if we are at the end of the row we go to the next row
            return sudoku(grid, row+1, 0)        
    return False#if we hit this it means that we have iterated through every possiblity and there are no solutions
    

def check(grid, row, col, num):#checks all the sudoku parameters to see what numbers can be placed at a spot 
    for i in range(9):#checks the rows for the same number
        if grid[row][i] == num:
            return False
    for i in range(9):#checks the colums for the same number
        if grid[i][col] == num:
            return False
    boxrow = (row // 3) *3 #making new indeicies for our 3 x 3's 
    boxcol = (col // 3) *3
    for i in range(boxrow, boxrow+3):#checks the 3x3 "box" for any similar numbers
        for j in range(boxcol, boxcol+3):
            if grid[i][j] == num:
                return False
    return True#if it makes it through all the checks that number can be placed there
            

def main():
    userin = input("Enter puzzle file: ")#user enters the puzzle file
    dafile = open(userin, 'r')
    puzzle = []
    for i in dafile:#makes file into a 2D list to be useable by the functions
        splitted = i.split(' ')
        splitted.pop(-1)
        puzzle.append(splitted)
    print(userin)#prints the name of the file
    for i in puzzle:#prints unsolved puzzle from file
            for j in i:
                print(j, end = ' ')
            print('\n')
    print('\n')
    if sudoku(puzzle, 0, 0):#prints solved puzzle
        for i in puzzle:
            for j in i:
                print(j, end = ' ')
            print('\n')
    else:
        print('No solution found')#if there is no solution the program says so
main()

#TO DO
    #different solutons
        
