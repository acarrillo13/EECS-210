def sudoku(grid, row, col, solutions):#solves the sudoku
    if row > 8:
        solutions.append([row[:] for row in grid])#copies the grid to the solutions
        return True
    if grid[row][col] == '_':#checks for empty space
        for i in range(9):
            if check(grid, row, col, str(i + 1)):
                grid[row][col] = str(i + 1)
                if sudoku(grid, row, col, solutions):
                    return True
            grid[row][col] = '_' #backtracking
    else:#moves to next index
        if col < 8:
            return sudoku(grid, row, col + 1, solutions)
        elif col == 8:
            return sudoku(grid, row + 1, 0, solutions)
    return False

def check(grid, row, col, num):#checks the 3 parameters for a sudoku spot
    for i in range(9): #row check
        if grid[row][i] == num:
            return False
        
    for i in range(9):#col check
        if grid[i][col] == num:
            return False
        
    boxrow = (row // 3) * 3
    boxcol = (col // 3) * 3
    for i in range(boxrow, boxrow + 3):#3x3 check
        for j in range(boxcol, boxcol + 3):
            if grid[i][j] == num:
                return False
            
    return True

def main():
    solutions = []  # List to store solutions
    userin = input("Enter puzzle file: ")#userinput for puzzle
    dafile = open(userin, 'r')
    puzzle = []
    for i in dafile:#makes the file into an unsolved puzzle
        splitted = i.split(' ')
        splitted.pop(-1)
        puzzle.append(splitted)
    print(userin)#prints unsolved puzzle
    for i in puzzle:
        for j in i:
            print(j, end=' ')
        print('\n')
    sudoku(puzzle, 0, 0, solutions)#pass solutions list to the solver
    if solutions:#prints the solutions
        for index, solution in enumerate(solutions, start=1):
            print(f"Solution {index}:")
            for row in solution:
                print(' '.join(row))
            print()
    else:#if solutions is empty there are no solutions 
        print('No solution found')
    print(f'Number of solutions: {len(solutions)}')

main()
