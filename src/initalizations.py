"""Variable initializations for the main scheduler"""

import csv
from itertools import combinations

# Remove Hardcoded Values and Use Functions to Determine them Instead
AVAILABLE_PADDING = 3
AVAILABLE_POSITION_START = 8
SHIFT_PADDING = 1
working_set = set()
day_index = 1
worker_num = 0


def init_vars(AVAILABILITY_GRID, SHIFT_GRID, fill_matrix):
    # Variables that offset information in CSV

    AVAILABILITY_FILE = open('../data/data_rep.csv')
    f_csv = csv.reader(AVAILABILITY_FILE)
    for row in f_csv:
        AVAILABILITY_GRID.append(row)

    AVAILABILITY_FILE.close()

    SHIFT_FILE = open('../data/shift_class.csv')
    f_csv = csv.reader(SHIFT_FILE)
    for row in f_csv:
        SHIFT_GRID.append(row)

    SHIFT_FILE.close()

    avail_col_size = len(AVAILABILITY_GRID[0])
    avail_row_size = len(AVAILABILITY_GRID)
    shift_row_size = len(SHIFT_GRID)
    shift_col_size = len(SHIFT_GRID[0])

    weekday_check = 0

    # Convert to integers and check weekday opening hours
    for i in range(1, shift_row_size):
        for j in range(1, shift_col_size):
            SHIFT_GRID[i][j] = int(SHIFT_GRID[i][j])
            weekday_check += SHIFT_GRID[i][j]
        if weekday_check == 0:
            del SHIFT_GRID[i]
            shift_row_size -= 1
            i =- 1
        else:
            weekday_check = 0

    # Convert to integers
    for i in range(1, avail_row_size):
        for j in range(1, avail_col_size):
            AVAILABILITY_GRID[i][j] = int(AVAILABILITY_GRID[i][j])

    working_set = []
    # Fill the Fill Matrix
    for i in range(1, len(SHIFT_GRID)): #Weekday Iterator
        fill_matrix.append([])
        working_set.append(set())

        # Position Iterator
        for j in range(AVAILABLE_POSITION_START, avail_col_size - AVAILABLE_PADDING):
            fill_matrix[i - 1].append(set())

            # Person Iterator
            for k in range(1, avail_row_size):
                if (AVAILABILITY_GRID[k][j] > 0 and AVAILABILITY_GRID[k][i] > 0):
                    fill_matrix[i - 1][j - AVAILABLE_POSITION_START].add(k)
                    working_set[i - 1].add(k)

    worker_num = sum(SHIFT_GRID[day_index][1:len(SHIFT_GRID[0]) - 1])

    print(fill_matrix, "\n")

    possibility_matrix = []

    # Weekday Iterator
    for i in range(1, len(SHIFT_GRID)):
        # Position Iterator
        for j in range(1, len(SHIFT_GRID[0])):
            # Possibilities
