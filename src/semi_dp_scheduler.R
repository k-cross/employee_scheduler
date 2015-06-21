# Written by: K-Cross

# Major Changes
# * No more randomization, DP used and all outcomes are stored for a single day
# * Optimization factors are added

# Initialzed variables
availability = read.csv("../data/data_rep.csv")
shiftClass = read.csv("../data/shift_class.csv")

# Number of people
people = availability[,1]

# Initialize the position vectors for comparing choices
position = availability[, 9:(dim(availability)[2] - 2)]

# Availability based on what day of week
dayAvailability = availability[,2:8]
weekDaySum = rowSums(dayAvailability)

# Availability based on how many days can work
workTime = availability[,dim(availability)[2] - 1]

dayIndex = 0
daysOpen = 7

# Conditions
wdCondition = 0 # binary condition, 0 = false

optimizedSchedule = matrix("0", daysOpen, length(positions[1,]))
colnames(optimizedSchedule) = colnames(positions)
rownames(optimizedSchedule) = colnames(dayAvailability)


write.csv(optimizedSchedule, file = "../data/weekly_schedule.csv")
