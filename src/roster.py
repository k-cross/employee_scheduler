"""Roster Class is built mainly as a subclass
   for the main Schedule Class

   Notes: After working tests, convert from multidimensional lists to numpy and pandas objects/arrays"""

"""attach counter values to the names of people for the actual scheduler"""

import csv
from collections import OrderedDict
from itertools import combinations, permutations

class Roster:
    """Docstring Appeasment"""
    def __init__(self): 
 
        # Remove Hardcoded Values and Use Functions to Determine them Instead
        self._AVAILABLE_PADDING = 3
        self._AVAILABLE_POSITION_START = 8
        self._AFTER_LABELS = 1 # Variable that offsets tables with labels
        self._SHIFT_PADDING = 1
        self._OPT_POSITION_INDEX = 0
        self._OPT_EMPLOYEE_INDEX = 0
        self._OPT_DIFFICULTY_INDEX = 0

        # Variables
        self._AVAILABILITY_GRID = []
        self._SHIFT_GRID = []
        self._fill_matrix = []
        self._possibility_matrix = []
        self._avail_row_size = 0
        self._avail_col_size = 0
        self._shift_row_size = 0
        self._shift_col_size = 0
        self._workdays = 7
        self._worker_num = []
        self._working_set = []
        self._total_positions = 0

        self.csv_to_list()

        self._avail_col_size = len(self._AVAILABILITY_GRID[0])
        self._avail_row_size = len(self._AVAILABILITY_GRID)
        self._shift_row_size = len(self._SHIFT_GRID)
        self._shift_col_size = len(self._SHIFT_GRID[0])
        self._total_positions = self._shift_col_size - self._AFTER_LABELS - self._SHIFT_PADDING

        self.int_convert_and_validate()
        self.populate_fill()
        self.permutator()

    def __del__(self):
        del self._AVAILABILITY_GRID
        del self._SHIFT_GRID
        del self._fill_matrix
        del self._possibility_matrix
        print("\n\n Deleted Everything")

    def getVars(self):
        """ For Debugging """
        print(self._fill_matrix, self._worker_num, self._possibility_matrix)





################ Init Functions ######################
    def csv_to_list(self):
        availability_file = open('../data/data_rep.csv')
        f_csv = csv.reader(availability_file)
        for row in f_csv:
            self._AVAILABILITY_GRID.append(row)

        availability_file.close()

        shift_file = open('../data/shift_class.csv')
        f_csv = csv.reader(shift_file)
        for row in f_csv:
            self._SHIFT_GRID.append(row)

        shift_file.close()

    def populate_fill(self):
        """ This takes care of the internal fill matrix """

        # Fill the Fill Matrix
        for i in range(1, len(self._SHIFT_GRID)): #Weekday Iterator
            self._fill_matrix.append([])
            self._working_set.append(set())

            # Position Iterator
            for j in range(self._AVAILABLE_POSITION_START,
                           self._avail_col_size - self._AVAILABLE_PADDING):
                self._fill_matrix[i - 1].append(set())

                # Person Iterator
                for k in range(1, self._avail_row_size):
                    if(self._AVAILABILITY_GRID[k][j] > 0 and self._AVAILABILITY_GRID[k][i] > 0):
                        self._fill_matrix[i - 1][j - self._AVAILABLE_POSITION_START].add(k)
                        self._working_set[i - 1].add(k)

        for i in range(0, self._workdays):
            self._worker_num.append(sum(self._SHIFT_GRID[i + 1][1:self._shift_col_size - 1]))

    def int_convert_and_validate(self):
        """ Converts character numbers in grids to integers """
        weekday_check = 0

        # Convert to integers and check weekday opening hours
        for i in range(1, self._shift_row_size):
            for j in range(1, self._shift_col_size):
                self._SHIFT_GRID[i][j] = int(self._SHIFT_GRID[i][j])
                weekday_check += self._SHIFT_GRID[i][j]
            if weekday_check == 0:
                del self._SHIFT_GRID[i]
                self._shift_row_size -= 1
                self._workdays -= 1
                i -= 1
            else:
                weekday_check = 0

        # Convert to integers
        for i in range(1, self._avail_row_size):
            for j in range(1, self._avail_col_size):
                self._AVAILABILITY_GRID[i][j] = int(self._AVAILABILITY_GRID[i][j])

    def permutator(self):
        """ Takes permutations of a set and puts them in the possibility matrix """
        # Workday Iterator
        for i in range(0, self._workdays):
            self._possibility_matrix.append([])

            # Case that's impossible to satisfy
            if(self._worker_num[i] > len(self._working_set[i])):
                self._possibility_matrix[i].append(0)
                print("failure")
                continue

            # Permutations
            for p in permutations(self._working_set[i], self._worker_num[i]):
                temp_vector = self._SHIFT_GRID[i + self._AFTER_LABELS][self._AFTER_LABELS:-self._SHIFT_PADDING]
                self._possibility_matrix[i].append([])
                position_number = 0
                good_flag = True # Might not need
                optimizer_value = 0 # The value used in optimizer calculations

                # Position Iterator
                for j in range(0, self._worker_num[i]):
                    # Problem with iteration, must add another check condition
                    if(temp_vector[position_number] > 0):
                        if(p[j] in  self._fill_matrix[i][position_number]):
                            temp_vector[position_number] -= 1
                            self._possibility_matrix[i][len(self._possibility_matrix[i]) - 1].append(p[j])
                            if j > 2:
                                print(j)

                            # Optimizer Calculation
                            #if(self._AVAILABILITY_GRID[p[j]][self._avail_col_size - 3] == 1
                            #and self._SHIFT_GRID[i + 1][self._shift_col_size - 1]):
                            #    optimizer_value += 2

                            #if(self._AVAILABILITY_GRID[p[j]][self._avail_col_size - 2] == j):
                            #    optimizer_value += 1

                            #optimizer_value += self._AVAILABILITY_GRID[p[j]][i + 1]

                        else:
                            del self._possibility_matrix[i][len(self._possibility_matrix[i]) - 1]
                            good_flag = False
                            break
                    else:
                        position_number += 1
                        j -= 1

                if(good_flag):
                    #self._possibility_matrix[i][len(self._possibility_matrix[i]) - 1] = p
                    #self._possibility_matrix[i][len(self._possibility_matrix[i]) - 1].append(optimizer_value)
                    print(self._possibility_matrix[i][len(self._possibility_matrix[i]) - 1])
