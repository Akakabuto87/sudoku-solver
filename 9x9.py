import numpy as np
 #                  TODO: remove all len(prog) and put in 9 because we never work with other sizes
 # https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques
 # check if one number is only one place in row/column/square
def sudoku_reader(filename_as_string):
    sudoku_text = open(filename_as_string, "r")
    lines=sudoku_text.readlines()
    dimension = len(lines[0].strip())
    sudoku = np.empty((dimension,dimension), dtype=int)
    for i in range(dimension):
        for j in range(dimension):
            sudoku[i,j] = lines[i][j]
    return sudoku
    
def print_s(array): #                  TODO: do this again with print("text", end = ' ')
    width = 3 + 9
    namestr = [ name for name in globals() if globals()[name] is array ]
    print("\nArray variable name:   ", namestr[0])
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end= " ")
                print("{:^12}".format("-------"), end=" ")
                if j == 8:
                    print("\n")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end= " ")
            print("{:^12}".format(str(array[i,j]).replace(" ", "").replace("0", " ")), end= " ")
            if j == 8:
                print("\n")

def square_check():# Take out the options that are in the solution 3x3 squares
    progress = 0
    for num in range(1, 10):
        for i in range(0,9,3):
            for j in range(0,9,3):
                if num in prog[i:i+3,j:j+3] and num in sol[i:i+3,j:j+3]:
                    prog[i:i+3,j:j+3,num-1] = np.zeros((3,3))
                    progress += 1
                    print("removed option   ", num, "   from a square  ", i//3+1, j//3+1)
    return progress

    
def row_col_check(): # Take out the options that are in the solution row or column
    progress = 0
    for num in range(1, len(prog)+1):
        for i in range(len(prog)):
            if num in prog[i,:,num-1] and num in sol[i,:]:
                prog[i,:,num-1] = np.zeros(len(prog))
                progress += 1
                print("removed option   ", num, "   from a row      ", i+1)
                # print_s(prog)
                # print_s(sol)
            if num in prog[:,i,num-1] and num in sol[:,i]:
                prog[:,i,num-1] = np.zeros(len(prog))
                progress += 1
                print("removed option   ", num, "   from a column   ", i+1)
                # print_s(prog)
                # print_s(sol)
    return progress

def sol_update(): # updates solution if prog only has one
    progress = 0
    for i in range(len(prog)):
        for j in range(len(prog)):
            sum=np.sum(prog[i,j])
            if sol[i,j] == 0 and sum in prog[i,j]:
                sol[i,j] = sum
                print("updated a solution:   ", sum, "  at row  ", i+1, "  column  ", j+1)
                # print_s(prog)
                # print_s(sol)
                prog[i,:,sum-1] = np.zeros(len(prog))
                prog[:,j,sum-1] = np.zeros(len(prog))
                progress += 1
    return progress            





# ------------------------------------------------------------------------- lets go
sudoku = sudoku_reader("sudoku3.txt")
# print_s(sudoku)
sol = np.copy(sudoku)
prog = np.zeros((*sudoku.shape, sudoku.shape[0]), dtype= int)

for i in range(len(prog)):
    for j in range(len(prog)):
        if sol[i,j] == 0:
            prog[i,j] = list(range(1, len(prog) + 1))




# ------------------------------------ solver loop
keep_going = True
cycle = 1
print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||||||\n Let's see the puzzle..:")

print_s(sol) 
print_s(prog)

while keep_going:
    print(" \n \n \n \n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
||||||||||||||||||||||||||||||||||||||||||\n \nRun Number. ", cycle)
    square_changes = square_check()
    row_col_changes = row_col_check()
    solution_progress = sol_update()
    
    
    
    
    
    
    
    
    
    print("Options removed squares:                  ", square_changes)
    print("Options removed from rows and columns:    ", row_col_changes)
    print("solutions filled out:                     ", solution_progress)
    
    print_s(sol)
    print_s(prog)    
    
    
    
    
    
    
    if row_col_changes == 0 and solution_progress == 0:
        keep_going = False
        print("\nBuuuuuuuuhhh.. Cannot make progress.     \nNeed more features")
    elif 0 not in sol:
        keep_going = False
        print("\nYay. I think I have solved the puzzle!!!")
    
    cycle += 1

