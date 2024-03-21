def sudoku(grid, row, col, solutions):#solves the sudoku
    if row == 9:
        solutions.append([row[:] for row in grid])#copies the grid to the solutions
        return True

    if grid[row][col] == '_':#checks for empty space
        for num in range(1, 10):
            if check(grid, row, col, str(num)):
                grid[row][col] = str(num)
                next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
                if sudoku(grid, next_row, next_col, solutions):
                    grid[row][col] = '_'  #backtracking
                    continue
                grid[row][col] = '_'  #backtracking
    else: #moves to next row or col after checking to see if it was empty
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if sudoku(grid, next_row, next_col, solutions):
            return True
    return False

def check(grid, row, col, num):#checks to see if a number fits for an empty space
    #returns false if num is equal to something else in the row, col, or box 
    for i in range(9):
        if grid[row][i] == num:#checks row
            return False
        if grid[i][col] == num:#checks col
            return False
    #checks 3x3 boxes
    boxrow = (row // 3) * 3
    boxcol = (col // 3) * 3
    for i in range(boxrow, boxrow + 3):
        for j in range(boxcol, boxcol + 3):
            if grid[i][j] == num:
                return False
    return True

def main():
    solutions = []#list to store solutions
    userin = input("Enter puzzle file: ")#gets file from user
    with open(userin, 'r') as dafile:#makes file into puzzle to be used by sudoku
        puzzle = [line.split() for line in dafile]

    print("Unsolved puzzle:")
    for row in puzzle:#prints unsloved puzzle
        print(' '.join(row))

    sudoku(puzzle, 0, 0, solutions)#starts to solve puzzle

    if solutions:#checks to see if there is something in solutions, if not it returns no solution found
        print("\nSolutions:")
        for index, solution in enumerate(solutions, start=1):#goes through solutions list printing each solution
            print(f"Solution {index}:")
            for row in solution:
                print(' '.join(row))
            print('\n')
    else:#no solutions in the solutions list
        print('No solution found')
    print(f'Number of solutions: {len(solutions)}')#prints total number of solutons

main()
