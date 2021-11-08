#This program calculates the arrival time of a flight based on
#user inputs of departure time and flight time 

#The function definition arrivalTime which calculates the
#arrival time of a flight based on inputs given

def arrivalTime (departureTimeMinutes, flightTimeMinutes, 
                 departureTimeHours, flightTimeHours):

#Where the function call variables are assignned to the
#local variables of the function definition

    departureTimeMinutes = dprtMins
    flightTimeMinutes = flghtMins
    departureTimeHours = dprtHours
    flightTimeHours = flghtHours

#The equations that calculate the arrivaltimeHours and
#arrivaltimeMinutes based on the user's input
    
    arrivaltimeHours = departureTimeHours + flightTimeHours
    arrivaltimeMinutes = departureTimeMinutes + flightTimeMinutes

#The conditionals that modify the values given from
#arrivaltimeMinutes and arrivaltimeHours into a readable
#form for the user

    if arrivaltimeHours > 12:
        arrivaltimeHours = arrivaltimeHours - 12
    
    if arrivaltimeMinutes > 59:
        arrivaltimeMinutes = arrivaltimeMinutes - 60
        arrivaltimeHours = arrivaltimeHours + 1
        if arrivaltimeHours > 12:
            arrivaltimeHours = arrivaltimeHours - 12

#The print statements that print out the output of
#arrivaltimeHours and arrivaltimeMinutes in a standard
#time format

    if arrivaltimeMinutes < 10:
        print("You will arrive at your destination at " 
              + str(arrivaltimeHours) + ":0", end="")
        print(str(arrivaltimeMinutes))
    else:
        print("You will arrive at your destination at " 
              + str(arrivaltimeHours) + ":", end="")
        print(str(arrivaltimeMinutes))

#The variables used for the function call

dprtHours = int(input("At what hour does your flight depart?"))
dprtMins = int(input("and how many minutes?"))
flghtHours = int(input("How many hours is your flight?"))
flghtMins = int(input("and how many minutes?"))

#Function call
arrivalTime(dprtMins, flghtMins, dprtHours, flghtHours)


    





