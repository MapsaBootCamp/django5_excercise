import numpy as np
table=[ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]


def row_check(table:list,num:int ,row:int):
    for col in range (9):
        if table[row][col]==num:
            return False
        
    return True
    
def col_check(table:list,num:int ,col:int):
    for row in range (9):
        if table[row][col]==num:
            return False   
    return True    

    
def sq_check(table:list,num:int,row:int , col:int):
    for rows in range((row//3)*3,((row//3)*3)+3):
        for cols in range((col//3)*3,((row//3)*3)+3):
            if table[rows][cols]==num:
                return False
    return True
    # startcolumn = col - col % 3  
    # startrow = row - row % 3 

    # for i in range(3):  
    #     for j in range(3):
    #         if table[startrow + i][startcolumn + j] == num:
    #             return False
    # return True


def sudoku_solve():
    global table
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                for num in range(1, 10):
                    if row_check(table,num,i):
                        if col_check(table,num,j): 
                            if sq_check(table,num,i,j):
                                table[i][j] = num
                                sudoku_solve()
                                table[i][j] = 0
                                print(np.matrix(table),end="\n\n\n")
                return
    print(np.matrix(table))
    
# def sudoku_solve(table:list,n:int):
#     index_holder=[]
#     for i in range(n):
#         for j in range(n):
#             if table[i][j]==0:
#                 for num in range(1,10):
#                     if row_check(table,num,i,j) and col_check(table,num,i,j) and sq_check(table,num,i,j):
#                         table[i][j]=num
#                         index_holder.append((i,j))
#                         break
#             if table[i][j]==0:
#                 for elm in reversed(index_holder):
#                     i,j=elm[0],elm[1]
#                     for num in range(table[i][j]+1,10):
#                         if row_check(table,num,i,j) and col_check(table,num,i,j) and sq_check(table,num,i,j):
#                             table[i][j]=num
#                             break
#                         else:
#                             table[i][j]=0
#                             sudoku_solve(table,n)
#     print(table)


sudoku_solve()