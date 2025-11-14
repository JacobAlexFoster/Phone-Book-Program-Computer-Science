import sys

def loop():
    print(""" 
    Phone Book Directory Computer Science v1.01
    1 - PhoneBook contents
    2 - Edit a Phone number
    3 - Add a Phone number
    4 - Remove a Phone number
    5 - Name lookup
    6 - Quit
    """)

    x = int(input("Enter a number from the directory to select an action: "))
    print("\n"*100)
    if x == 1:
        print("Phone Book Contents: ")
        file = open("pb.txt")
        print(file.read())
        file.close()
    elif x == 2:
        print("test")
    elif x == 3:
        newName = input("Enter the name of the person to be added: ")
        newNumber = int(input("Enter the new contacts number: "))
        file = open("pb.txt","a")
        file.write("\n" + newName + ": " + str(newNumber))
        file.close()
        file = open("pb.txt")
        print(file.read())
        file.close()
        loop()  
    elif x == 4:
        nameToRemove = input("Enter the name of the contact to remove: ")
        with open("pb.txt", "r") as file:
            lines = file.readlines()
        with open("pb.txt", "w") as file:
            removed = False
            for line in lines:
                if line.strip().startswith(nameToRemove + ":"):
                    removed = True
                    continue
                file.write(line)
        if removed:
            print(f"{nameToRemove} has been removed from the phone book.")
        else:
            print(f"{nameToRemove} not found in the phone book.")
        with open("pb.txt", "r") as file:
            print("Updated Phone Book Contents:\n")
            print(file.read())
        loop()

    elif x == 5:
        nameToLookup = input("Enter the name to look up: ")
        found = False
        with open("pb.txt", "r") as file:
            for line in file:
                if line.strip().startswith(nameToLookup + ":"):
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        print(f"{parts[0]}'s phone number is {parts[1].strip()}")
                        found = True
                    break

    if not found:
        print(f"{nameToLookup} not found in the phone book.")

    elif x == 6:
        sys.exit()
    else:
        loop()
loop()