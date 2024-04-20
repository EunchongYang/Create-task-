
classschedule = {}

def scheduleyourclass(classschedule):
    classname = input("Enter your class name: ")
    day = input("What day(s) do you have this class (e.g., Tuesday): ")
    time = input("Enter the time (e.g., 11:00 AM): ")
    classschedule[classname] = [day, time]
    print("A new class is added to your schedule " + classname + " on " + day + " during " + time)

def deleteclass(classschedule):
    classname = input("What class would you like to delete? ")
    if classname in classschedule:
        del classschedule[classname]
        print("Your class " + classname + " has been deleted")
    else:
        print("Class name was not found in the schedule. Try again")

def viewschedule(classschedule):
    for key in classschedule:
        print("Your class", key, "is on", classschedule[key][0], "at", classschedule[key][1])

def manageschedule(classschedule):
    choice = "1"
    while choice != "4":
        print("Class scheduler")
        print("1. Add a class")
        print("2. Delete a class")
        print("3. View class schedule")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            scheduleyourclass(classschedule)
        elif choice == '2':
            deleteclass(classschedule)
        elif choice == '3':
            viewschedule(classschedule)
        elif choice == '4':
            print("Thank you for using the class scheduler. Have a good day!")
        else:
            print("Invalid choice. Please try again.")

manageschedule(classschedule)
