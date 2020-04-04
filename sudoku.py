from itertools import permutations
import random
import sys
random.seed(5180044)
#Check if the list has duplicate tuple
def check_dup(x):
    for i in zip(*x):
        if len( set(i))!=3:
            return False
    return True


def create_sudoku():
    base =[]
    perm = permutations([0,1,2])
    #Create a base with permutation of 0,1,2
    for i in list(perm):
        base.append(i)
    table = []
    base_num=[(0, 1, 2), (2, 0, 1), (1, 2, 0)]
    while len(table)<9:
        temp=[]
        for i in range(3):
            temp.append(random.choice(base))
        if check_dup(temp)!=False and not temp in table:
            table.append(temp)
    #Turn table of 0,1,2 to board with number from 1 to 9
    board = []
    for k in range(0,9):
        board2=[]
        for i in range(0,3):
            for j in range(0,3):
                board2.append(base_num[k//3][k%3]*3 + table[k][i][j] + 1)
        board.append(board2)

    #swap 2nd and 4th row
    for i in range(0,3):
        for j in range(3,6):
            board[i][j],board[i+3][j-3]=board[i+3][j-3],board[i][j]
    #swap 3rd and 7th row
    for i in range(0,3):
        for j in range(6,9):
            board[i][j],board[i+6][j-6]=board[i+6][j-6],board[i][j]
    #swap 6rd and 8th row
    for i in range(3,6):
        for j in range(6,9):
            board[i][j],board[i+3][j-3]=board[i+3][j-3],board[i][j]
    return board
#Create holes to board with given number of holes
def put_holes(board,n):
    if n == 0:
        return board 
    else:
        for j in range(0,9):
            i=0
            while i<n//9:
                temp=random.randrange(0,9)
                if board[j][temp]!=0:
                    board[j][temp]=0
                    i+=1
    return board


#Change the rows and columns of board to appropriate sudoku form
def Organize_board(board):
    block_1=[]
    block_2=[]
    block_3=[]
    block_4=[]
    block_5=[]
    block_6=[]
    block_7=[]
    block_8=[]
    block_9=[]

    for i in range(0,3):
        for j in range(0,3):
            block_1.append(board[i][j])
    for i in range(0,3):
        for j in range(3,6):
            block_2.append(board[i][j])
    for i in range(0,3):
        for j in range(6,9):
            block_3.append(board[i][j])
    for i in range(3,6):
        for j in range(0,3):
            block_4.append(board[i][j])
    for i in range(3,6):
        for j in range(3,6):
            block_5.append(board[i][j])
    for i in range(3,6):
        for j in range(6,9):
            block_6.append(board[i][j])
    for i in range(6,9):
        for j in range(0,3):
            block_7.append(board[i][j])
    for i in range(6,9):
        for j in range(3,6):
            block_8.append(board[i][j])
    for i in range(6,9):
        for j in range(6,9):
            block_9.append(board[i][j])
    complete_sudoku = []
    complete_sudoku.append(block_1)
    complete_sudoku.append(block_2)
    complete_sudoku.append(block_3)
    complete_sudoku.append(block_4)
    complete_sudoku.append(block_5)
    complete_sudoku.append(block_6)
    complete_sudoku.append(block_7)
    complete_sudoku.append(block_8)
    complete_sudoku.append(block_9)
    return complete_sudoku
   
if __name__=='__main__':
    parameter = sys.argv
    if int(parameter[1]) % 9 != 0:
        print('Input must be multiple of 9 !')
    elif int(parameter[1]) > 81:
        print('Out of range !')
    else: 
         filename = parameter[2]
         myfile = open(filename,'w')
         for i in Organize_board(put_holes(create_sudoku(),int(parameter[1]))):
           s = ", ".join(map(str,i))
           for j in s:
            myfile.writelines(j)
           myfile.write("\n")
         myfile.close()














