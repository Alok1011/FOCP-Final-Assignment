from os import system

system("cls")
speed_list=[]
count=0
total=0

print("Swallow Speed Analysis: Version 1.0\n")

while True:
    reading=input("Enter the Next Reading:")

    # If the user presses enter then the value in the list are calculated for the final output and displayed.
    if (reading == ""):

        avg=sum(speed_list)/len(speed_list)

        print("\nResults Summary\n")
        print(count,"Reading Analysed.\n")
        print("Max Speed: {:.2f} MPH {:.2f} KPH".format(max(speed_list)/1.60934,max(speed_list)))
        print("Min Speed: {:.2f} MPH {:.2f} KPH".format(min(speed_list)/1.60934,min(speed_list)))
        print("Avg Speed: {:.2f} MPH {:.2f} KPH".format(avg/1.60934,avg))

        break

    # If the reading's initial contains "E" or "U" then the value is checked, converted and stored in list.
    elif (reading[0].upper()=="E" or reading[0].upper()=="U"):
        check=0
        for x in reading[1:]:
            if x.isalpha()==True:
                check+=1
   
        if check==0:
            print("Reading Saved.")

            # Converting the value into same unit (miles) and adding them to the list.
            if reading[0].upper() == "U":
                num=(float(reading[1:])*1.60934)
            else:
                num=float(reading[1:])

            speed_list.append(num)
            count+=1
        else:
            print("ERROR! The speed could not be processed!")

    else:
        print("ERROR! The initials entered could not be processed!")