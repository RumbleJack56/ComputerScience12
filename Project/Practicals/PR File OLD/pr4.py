print("Leap Year Finder")
yr = int(input("Please input year: "))
if (((yr%4==0) and (yr%100!=0)) or (yr%400==0) ):
    print("The year",yr,"is a leap year.")
else:
    print("The year",yr,"is not a leap year.")
