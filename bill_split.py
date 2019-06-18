total = float(input("Please enter amount: "))   # Total amount
i = 0           # loop holder
nameList = {}   # List of names and amount
newTotal = 0    # To hold remainder of total

# Entering each person's name
print("Enter 'Done' once everyone's name is in")
while i == 0:
    newName = input("Enter name: ")

    # Break from loop when done
    if newName == "Done" or newName == "done":
        i = 1
        break
    else:
        nameList.update({newName: 0})

    # Show current name list
    print("Name list:")
    for name in nameList:
        print(name)
    
    print()

# Show the dictionary
print(nameList)
print()

# Show the current amount entered and balance remaining
def check_balance():
    curr = 0.0      # Current total amount added so far
    for value in nameList.values():
        curr += value

    print("*************************")
    print("Current total: %0.2f" % curr)
    print("Current balance: %0.2f" % (total - curr))
    print(nameList)
    print()

    # Update remainder value
    global newTotal 
    newTotal = total - curr

    # Checks of balance of 0 is reached
    if total - curr == 0:
        print("Balance is zero")
        return 1
    # Checks if balance is negative
    # If so need to redo
    elif total - curr < 0:
        print("Something is wrong. Please recheck calculations")
        return 2
    else:
        return 0

# Add amount entered to dictionary
def add_val(name, amt):
    nameList[name] += amt

print("Please enter the name of the person that you want to enter amount of")
print("Enter 'Exit' to exit and enter new name")
print("Enter 'Done' when prompt to enter name to split the rest of balance")

# Select which person
while i == 1:
    tempName = input("Please enter a name: ")

    if tempName == "Done" or tempName == "done":
        break
    elif tempName not in nameList:
        print("*************************")
        print("ERROR")
        print("No such name. Please check")
        continue
    
    # Enter amount item by item
    while check_balance() == 0:
        tempAmt = input("Please enter sub-cost for %s: " % tempName)

        # Exit if want to move on to next person
        if tempAmt == "Exit" or tempAmt == "exit":
            break
        
        add_val(tempName, float(tempAmt))

    if check_balance() == 1:
        print("Everything is balanced")
        break
    elif check_balance() == 2:
        for currName in nameList:
            nameList[currName] = 0.0

        print("Calculation reset. Please redo")
        print()

# Split the balance equally
print()
print("*************************")
print("Splitting the balance equally")
print("Remainder: %0.2f" % newTotal)
newSplit = newTotal/len(nameList)
print("Split among %i people: %0.2f" % (len(nameList), newSplit))

for name in nameList:
    nameList[name] += newSplit
    
print(nameList)

# Calculate WI tax
print()
print("*************************")
print("Calculating what everyone has to pay plus tax")
print("Tax: WI, 5.5%")
for currName in nameList:
    payThis = nameList[currName] * 1.055
    nameList[currName] = payThis
    print("%s pays %0.2f" % (currName, payThis))

print()
tipOrNah = input("Need 15% tip? (Y/N): ")

# Calculate for tips
if tipOrNah == "Y" or tipOrNah == "y":
    for currName in nameList:
        nameList[currName] = nameList[currName] * 1.15
        print("%s pays %0.2f" % (currName, nameList[currName]))