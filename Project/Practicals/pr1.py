print("Temperature of the week (⁰C)")    #Title

#Obtain Temperature input from user
tempMon=float(input("Enter Temperature on Monday   (⁰C): "))
tempTue=float(input("Enter Temperature on Tuesday  (⁰C): "))
tempWed=float(input("Enter Temperature on Wednesday(⁰C): "))
tempThu=float(input("Enter Temperature on Thursday (⁰C): "))
tempFri=float(input("Enter Temperature on Firday   (⁰C): "))
tempSat=float(input("Enter Temperature on Saturday (⁰C): "))
tempSun=float(input("Enter Temperature on Sunday   (⁰C): "))

tempAvg=(tempMon + tempTue + tempWed + tempThu + tempFri + tempSat + tempSun)/7 #Average Temperature
tempAvg = (tempAvg//0.01)/100    #removes everything after 2 decimals

print("The average temperature of the week was ",tempAvg,"⁰C",sep="")     #Output
