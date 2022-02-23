import csv
import random

def booking():
    bookings = []
    bookingref = random.randint(0,100)
    bookingref = str(bookingref)
    print("The booking ref is :", bookingref)
    surname = input("Please enter your surname: ")
    forename = input("Please enter your forename: ")
    bookings.append(bookingref)
    bookings.append(surname)
    bookings.append(forename) 
    print("********Following are the latest releases********")
    l=["Spiderman: No Way Home","Gehraiyaan","Hridayam"," Matrix: Resurections ","The Batman"]
    print(l)
    film = input("Please enter the film you would like to see: ")
    for i in range(0,len(l)):
        if l[i]==film:
            bookings.append(film)
            break
    else:
        print("error")
    l2=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
    day=input("What day of the week do you want to see the film?: ")
    for i in range(0,len(l2)):
        if l2[i]==day:
            bookings.append(day)
            break
    else:
        print("error")
    print("********Following are the time slots available********")
    l3=["9.00 am","1.00 pm","4.00 pm","6.00 pm","9.00 pm"]
    print(l3)
    time = input("Enter a time from the above slots: ")
    for i in range(0,len(l3)):
        if l3[i]==time:
            bookings.append(time)
            break
    else:
        print("error") 
    print("/////////// Booking successful///////////")
    with open("cinema.csv","a",newline='')as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(bookings)
        
def confirmbooking():
    with open("cinema.csv","r")as csvfile:
        r=csv.reader(csvfile)
        refno=input("Enter refrence number: ")
        for i in r:
                if i[0]==refno:
                    print("")
                    print("/////////////////////////////////////////")
                    print("REFRENCE NUMBER : ",i[0])
                    print("NAME            : ",i[2],i[1])
                    print("FILM            : ",i[3])
                    print("DAY             : ",i[4])
                    print("TIME            : ",i[5])
                    print("/////////// Booking confirmed ///////////")
                    print("") 
                    break
        else:
            print("/////////// Sorry, not found /////////// ")
               
print("########### Welcome to the cinema booking system ###########")
while True:
    print("Enter 1: Book a film")
    print("Enter 2: Confirm booking")
    print("Enter 3: Exit")
    choice = input("Please select an option from above: ")
    if choice=="1":
        booking()
    elif choice=="2":
        confirmbooking()
    elif choice=="3":
        print("########### THANK YOU ###########")
        break
