"""Main Function for scheduling logic"""

import csv, time
from itertools import combinations
from roster import Roster

# Initalization of Parameters
# Need to change CSV values from str/char to Int

start_time = time.time()

TEST = Roster()

TEST.getVars()

print("%s seconds --" %(time.time() - start_time))
