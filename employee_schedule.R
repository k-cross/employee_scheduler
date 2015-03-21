#Written by: Kenneth Cross

#This program was built to make a schedule based on a CSV file
#The first row is names, the next seven columns are days of the week, the next columns
#are job positions, the penultimate row is the amount of days a person can work
#and the last row is a potential optimizer, based on the person's performance
#to give better shifts to that person as a reward.

#To-Do: "Optimizer" needs to be implemented
#       "Mandatory" column designed to make sure this person recieves this many days of work
#       Perhaps some user friendliness

#initialzed variables
#Store the schedule data in schedule

#Randomizes the row order for different outcomes upon each run
#this is to avoid favoritism due to the algorithmic method
schedule = read.csv("availability.csv")
randVector = runif(length(schedule[,1]))
schedule = schedule[order(randVector),]

#scheduler = function(schedule){

#Number of people
people = schedule[,1]

#initialize the position vectors for comparing choices
positions = schedule[, 9:(dim(schedule)[2] - 2)]

#availability based on what day of week
availability = schedule[,2:8]
weekDaySum = rowSums(availability)

#availability based on how many days can work
workTime = schedule[,dim(schedule)[2] - 1]

dayIndex = 0
daysOpen = 7

optimizedSchedule = matrix("0", daysOpen, length(positions[1,]))
colnames(optimizedSchedule) = colnames(positions)
rownames(optimizedSchedule) = colnames(availability)

#creating general algorithm for schedule
while(dayIndex < daysOpen){
    positionIndex = 0
    personIndex = 0
    scheduleIndex = 0

    while(scheduleIndex < length(positions[1,])){
        if(optimizedSchedule[dayIndex+1, positionIndex+1] == "0"){
            if(positions[personIndex+1,positionIndex+1] == 1){
                if(availability[personIndex+1,dayIndex+1] > 0 && workTime[personIndex+1] > 0){
                    optimizedSchedule[dayIndex+1, positionIndex+1] = as.character(people[personIndex+1])
                    workTime[personIndex+1] = workTime[personIndex+1] -1
                    positionIndex = positionIndex + 1
                    personIndex = personIndex + 1
                    scheduleIndex = scheduleIndex + 1
                    if(positionIndex > length(positions[1,])-1){
                        positionIndex = 0
                    }
                } else{
                    personIndex = personIndex+1
                    positionIndex = 0
                    if(personIndex > length(people)-1){
                        personIndex = 0
                    }
                }
            } else{
                positionIndex = positionIndex+1
                if(positionIndex > length(positions[1,])-1){
                    positionIndex = 0
                    personIndex = personIndex + 1
                    if(personIndex > length(people)-1){
                        personIndex = 0
                    }
                }
            }
        } else{
            positionIndex = positionIndex + 1
            if(positionIndex > length(positions[1,])-1){
                positionIndex = 0
                personIndex = personIndex + 1
                if(personIndex > length(people)-1){
                    personIndex = 0
                    scheduleIndex = scheduleIndex + 1
                }
            }
        }
    }

    dayIndex = dayIndex+1
}
#}
#debug(scheduler)

write.csv(optimizedSchedule, file = "weekly_schedule.csv")
