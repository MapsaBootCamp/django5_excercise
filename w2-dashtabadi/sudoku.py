from typing import List


def is_safe(grid: List[List[int]],
            row: int,
            col: int,
            num: int) -> bool:
    """ number can be assign to the cell?
    :param grid:
    :param row: row of array
    :param col: col of array
    :param num: number to be checked.
    :return:
    """

    # same num found in row?  if found then return False
    for x in range(9):
        if grid[row][x] == num:
            return False

    # same num found in column? if found then return False
    for x in range(9):
        if grid[x][col] == num:
            return False

    # same num found in 3*3? if found then return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False

    # If it has passed the previous steps, so num is correct
    return True


def sudoku_solver(grid, row, col, size=9):
    # we solved the sudoku?
    if (row == size - 1 and col == size):
        return True

    # if col becomes 9 then move to next row / column start from 9
    if col == size:
        row += 1
        col = 0

    # if (cell-value > 0) so it's solved then we move to next column
    if grid[row][col] > 0:
        return sudoku_solver(grid, row, col + 1)

    for num in range(1, size + 1, 1):
        # can we add number (1-9) to the cell? then go to the next column
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if sudoku_solver(grid, row, col + 1):
                return True

        # due to wrong num to assign into cell, we check further num
        grid[row][col] = 0

    return False


if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if (sudoku_solver(grid, 0, 0, 9)):
        printing(grid)
