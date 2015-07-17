"""Main Function for scheduling logic"""

import csv
from itertools import combinations
from initalizations import init_vars

# Initalization of Parameters
# Need to change CSV values from str/char to Int

AVAILABILITY_GRID = []
SHIFT_GRID = []

taboo = []
fill_matrix = []

# [][][][] 0) Weekday 1) Possibility 2) Position 3) Employees Filling
possibility_matrix = []

init_vars(AVAILABILITY_GRID, SHIFT_GRID, fill_matrix)

# For combinations use sets and lists
